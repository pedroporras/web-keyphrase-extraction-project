import time
import jwt
from decouple import config


JWT_SECRET = config('secret')
JSWT_ALGORITHM = config('algorithm')


def token_response(token: str) -> dict:
    """
    Return generate tokens (JWTs)
    """
    return {
        "access_token": token,
    }

def signJWT(userID: str) -> str:
    """
    Sign JWT with userID
    """
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    """
    """
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JSWT_ALGORITHM)
        return decode_token if decode_token['expiry'] > time.time() else None
    except:
        return {}
        