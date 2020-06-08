from Crypto.PublicKey import RSA
from ast import literal_eval
import jose.jwk as jwk
import jose.jwt as jwt
import time
import uuid
import os


class JWT():
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
        my_jwk = None
        my_pem = None

        # check if JWK
        if ((type(private_key) == str and private_key.startswith("{")) or
                type(private_key) == dict):
            if (type(private_key) == str):
                private_key = literal_eval(private_key)

            my_jwk = jwk.construct(private_key, JWT.HASH_ALGORITHM)
        else:  # it's a string
            # check for filepath or explicit private key
            if os.path.exists(private_key):
                pem_file = open(private_key, 'r')
                my_pem = RSA.import_key(pem_file.read())
                pem_file.close()
            else:
                private_key_bytes = bytes(private_key, 'ascii')
                my_pem = RSA.import_key(private_key_bytes)

            if not my_pem:
                return (None, ValueError(
                    "RSA Private Key given is of the wrong type"))

        if my_jwk:  # was JWK
            # get PEM using JWK
            pem_bytes = my_jwk.to_pem(JWT.PEM_FORMAT)
            my_pem = RSA.import_key(pem_bytes)
        else:  # was pem
            # get JWK using PEM
            my_jwk = jwk.construct(my_pem.export_key(), JWT.HASH_ALGORITHM)

        return (my_pem, my_jwk)

    @staticmethod
    def create_token(org_url, client_id, private_key):
        my_pem, my_jwk = JWT.get_PEM_JWK(private_key)
        issued_time = int(time.time())
        expiry_time = issued_time + JWT.ONE_HOUR
        generated_JWT_ID = str(uuid.uuid4())

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
