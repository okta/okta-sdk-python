from okta.client import Client
import asyncio

pem_key='''-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDUqh8xBac0HlQe
euxSwmLPoEzjO/gjSpa+dzg2kXQvbAqA4LGiA4iVAT0UcPGtiyWyKYMXpzezj7/U
NPezjmoDzfPUDWZoCASzRdBM+4NOiqsUgNjwVsip9LVg9ALFEV+C3oCEhY2Gh3e9
OzbmNycobZjRrAexrg/XdTkA6AqtobXpHBsF+7/7I7mEHPvVajLuX3C5/bHYUaMb
dyfYFGESr/ZaVTOcaZ8pbkr3zXtHa5sERihFm8v9TiI68PyIadQcN5pf0e1axvC5
JhKqsJvbuO0Ja/TVOiEnJr/nHDu0h5fjp/cP1kyQ+OD7uktQ3r0v9LeEcohnty5E
alK9HO15AgMBAAECggEAHrpkHmO4OK4nLm5Jhl3DBEgfw/euz36gEG5Oh4f110JP
tDaDRCspiYovxqvZJ9/Ctx8La5gEUuQy7hknL2ElDV6tXBcBlIeQEk1En1L6MpeT
x7ckYXnQrcoHiTZIzivH9rNqs3tOq0EYupV7RcFzXYKUgbtPM0u4y0OLVIeyv0qq
dZ/FsLYedlqCfKsNfCPpZK2jgtXtgOOqr82Xxwg7UMJfSDH2XDxt6z3pv3Ty0ijA
v7RYlpRr6kyiDQ3fHsPgNUNOb5lwI4GsGkxZG9Uiy5+SkwHQLqhWIxogpmlbCFjw
vmv5XP8yXXHjZgWHPsA4efQSqTmT+3yBLcXSpYgI5wKBgQDwtvwt3gbfI1X/4cW1
utHzU2KTNJClfGz9EdGCx26F+2sYQMYqwAKPWqU8j2NuTGjC2IjIMp50Wtw9NzTh
dZEoURLyZB8BqH9k0/pgb7en00jvLgtyzH6c3RJ40xiJVdBO2VlJSL4Q4pnoRNZ2
YPx6EKKwGq/+TkSZAxGxGhI5EwKBgQDiKyg7HAomRHfa/U9O4oBqvGolUxqA+cuL
mV3ad7cigHscSkSG5wFzHPWOBrGoHPbKJ6DD5lsfvEZVRNXMCRnFImHNVVxyC07e
qTy+Z4SmGZgeVhoC4TVB09oGlk4w3vCRd/BBGeYPu7gRHXyRTbTyYU86UuxQrVac
md6Z8xk8wwKBgQCmmC3t3KTq17zUTEAWJwbZHZOyh4W4UmXnu+ZBWZ8fcULMVUAR
JDRhXH3RbPeGxbEXcN8xlv7dTmjwoP2jMEfXHE09npdrAV+xu5ekGI2FxA/NIRPh
TrAuBj6bipWHrvFtMLW/p22LqBiWjNXUtgjmvg6qTL4TBb4qG9qptH56KwKBgQC/
RoSVyRcEWi+Lc2QZcRHuMz8KJghqP9hXTfPECi9F7Kcxu9XMyZ2+PyWlYh/p7+T/
/xfF1hIG+vH4t2ihUKkMwhE42RKAGPQw96w5086ps0elkGgbO2ARNhxUKdYjGskW
HfuA82hQsg/v2aI6OR/pRUb+KpdVe+OeObu7M4+KhQKBgQC1smUHvYFQimyhOcA2
B5b9M0q+cUknMwM9GbgNT1sV6tkYlj6Va86DzFEVqmkBU42y4jm/3ChPXlmuC4Nv
l4s4uWqf8JX7GExXfrd0ERy713NlLEBW5c66RaTI4k9YoPoWI4rc91FGhBIVkJV4
2l2MlYySZbX2T2crKlN4+ESg1Q==
-----END PRIVATE KEY-----'''

okta_client = Client({
    'orgUrl': 'https://trial-5149309.okta.com',
    'authorizationMode': 'PrivateKey',
    'clientId': '0oadsp75t8VEatJK1697',
    'scopes': ['okta.users.manage'],
    'privateKey': pem_key, # this parameter should be type of str
    'kid': 'bu5MAM6TzARaIcvJ9Q2NInbb7nkqIeVgh_VOuVHQnB4' # if a key ID needs to be provided, it can be provided here or part of the privateKey under "kid"})
})

user, res, err = asyncio.run(okta_client.get_user('00udsp6xx9iFA0mRr697'))

print(user)
print(res)
print(err)

asyncio.run(okta_client._request_executor._oauth.get_access_token())