from tutorial.settings import JWT_AUTH as jwta
import datetime


def jwt_response_payload_handler(token, user=None, request=None):
    print(user)
    return {
        'token': token,
        'user': user.username,
        'email': user.email,
        'expiry_date': jwta["JWT_REFRESH_EXPIRATION_DELTA"]
    }
