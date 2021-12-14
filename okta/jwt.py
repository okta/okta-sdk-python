from Crypto.PublicKey import RSA
from ast import literal_eval
import jose.jwk as jwk
import jose.jwt as jwt
import time
import uuid
import os


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
        if ((type(private_key) == str and private_key.startswith("{")) or
                type(private_key) == dict):
            # if string repr, convert to dict object
            if (type(private_key) == str):
                private_key = literal_eval(private_key)
            # Create JWK using dict obj
            my_jwk = jwk.construct(private_key, JWT.HASH_ALGORITHM)
        else:  # it's a PEM
            # check for filepath or explicit private key
            if os.path.exists(private_key):
                # open file if exists and import key
                pem_file = open(private_key, 'r')
                my_pem = RSA.import_key(pem_file.read())
                pem_file.close()
            else:
                # convert given string to bytes and import key
                private_key_bytes = bytes(private_key, 'ascii')
                my_pem = RSA.import_key(private_key_bytes)

            if not my_pem:
                # return error if import failed
                return (None, ValueError(
                    "RSA Private Key given is of the wrong type"))

        if my_jwk:  # was JWK provided
            # get PEM using JWK
            pem_bytes = my_jwk.to_pem(JWT.PEM_FORMAT)
            my_pem = RSA.import_key(pem_bytes)
        else:  # was pem provided
            # get JWK using PEM
            my_jwk = jwk.construct(my_pem.export_key(), JWT.HASH_ALGORITHM)

        return (my_pem, my_jwk)

    @staticmethod
    def create_token(org_url, client_id, private_key):
        """
        Create a JSON Web Token using Oauth details from the Okta Client
        config.

        Args:
            org_url (str): Okta Organization URL
            client_id (str): Client ID
            private_key (str or dict): Private Key representation

        Returns:
            str: Generated JWT
        """
        # Generate PEM and JWK
        my_pem, my_jwk = JWT.get_PEM_JWK(private_key)
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

        token = jwt.encode(claims, my_jwk.to_dict(), JWT.HASH_ALGORITHM)
        return token
