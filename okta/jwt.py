import json
import os
import time
import uuid

from ast import literal_eval
from Cryptodome.PublicKey import RSA
from jwcrypto.jwk import JWK, InvalidJWKType
from jwt import encode as jwt_encode


class JWT():
    """
    This class creates a JWT from the Okta Client configuration.
    """

    OAUTH_ENDPOINT = "/oauth2/v1/token"
    HASH_ALGORITHM = "RS256"
    PEM_FORMAT = "PKCS1"
    ONE_HOUR = 1 * 60 * 60
    JWT_OPTIONS = {
        'verify_signature': True,
        'verify_aud': True,
        'verify_iat': True,
        'verify_exp': True,
        'verify_nbf': True,
        'verify_iss': True,
        'verify_sub': True,
        'verify_jti': True,
        'verify_at_hash': True,
        'require_aud': True,
        'require_iat': False,
        'require_exp': True,
        'require_nbf': False,
        'require_iss': True,
        'require_sub': True,
        'require_jti': True,
    }

    def __init__(self, private_key):
        pass

    @staticmethod
    def get_PEM_JWK(private_key):
        """
        This class gets the PEM and JWK representation of the private key
        from the Okta Client configuration.

        Args:
            private_key (str or dict): Either a dict representing a JWK, str
            representing the JWK, filepath to PEM, or PEM string

        Returns:
            RSAKey, JWK: Tuple of the generated PEM, and JWK
        """
        # Start off with both as None
        my_jwk = None
        my_pem = None

        # check if JWK
        # String representation of dictionary or dict
        if ((isinstance(private_key, str) and private_key.startswith("{")) or
                isinstance(private_key, dict)):
            # if string repr, convert to dict object
            if isinstance(private_key, str):
                private_key = literal_eval(private_key)
            # remove whitespace from key vaules
            private_key = {k: ''.join(private_key[k].split()) for k in private_key}
            # ensure private_key is JSON formatted
            try:
                json.loads(private_key)
            except TypeError:
                private_key = json.dumps(private_key)
            try:
                my_jwk = JWK.from_json(private_key)
            except InvalidJWKType:
                raise ValueError(
                    "JWK given is of the wrong type")
        else:  # it's a PEM
            # check for filepath or explicit private key
            if isinstance(private_key, (str, bytes, os.PathLike)) and os.path.exists(private_key):
                # open file if exists and read
                pem_file = open(private_key, 'r')
                private_key = pem_file.read()
                pem_file.close()
            # remove leading whitespaces from each line
            my_pem = '\n'.join([line.strip() for line in private_key.splitlines()])
            my_pem = bytes(my_pem, 'ascii')
            try:
                my_jwk = JWK.from_pem(my_pem)
            except ValueError:
                raise ValueError(
                    "RSA Private Key given is of the wrong type")

        my_pem = my_jwk.export_to_pem(private_key=True, password=None)
        my_pem = RSA.import_key(my_pem)

        return (my_pem, my_jwk)

    @staticmethod
    def create_token(org_url, client_id, private_key, kid=None):
        """
        Create a JSON Web Token using Oauth details from the Okta Client
        config.

        Args:
            org_url (str): Okta Organization URL
            client_id (str): Client ID
            private_key (str or dict): Private Key representation
            kid (str): Key ID

        Returns:
            str: Generated JWT
        """
        # Generate PEM and JWK
        my_pem, _ = JWT.get_PEM_JWK(private_key)
        # Get current time and expiry time for token
        issued_time = int(time.time())
        expiry_time = issued_time + JWT.ONE_HOUR
        # generate unique JWT ID
        generated_JWT_ID = str(uuid.uuid4())

        # Create claims for token and create token
        claims = {
            'sub': client_id,
            'iat': issued_time,
            'exp': expiry_time,
            'iss': client_id,
            'aud': org_url + JWT.OAUTH_ENDPOINT,
            'jti': generated_JWT_ID
        }

        # Add additional headers
        headers = {}

        # # Check if kid was supplied
        if kid:
            headers["kid"] = kid
        elif isinstance(private_key, dict) and "kid" in private_key:
            headers["kid"] = private_key["kid"]
        elif isinstance(private_key, str):
            try:
                private_key_dict = json.loads(private_key)
                if "kid" in private_key_dict:
                    headers["kid"] = private_key_dict["kid"]
            except json.JSONDecodeError:
                if "kid" in headers:
                    del headers["kid"]

        token = jwt_encode(claims, my_pem.export_key(), JWT.HASH_ALGORITHM, headers)
        return token
