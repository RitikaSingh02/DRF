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


'''
what is a payload?:
https://stackoverflow.com/questions/55069938/jsonwebtoken-what-is-payload#:~:text=In%20JSON%20Web%20Tokens%2C%20the,data%20for%20a%20particular%20user.&text=However%2C%20it%20can%20also%20contain,name%2C%20language%20preferences%2C%20etc.
'''
