from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated
from models import utils
import jwt
import os
import bcrypt

oauth_bearer = OAuth2PasswordBearer('login')

def decode_user_token(token: str = Depends(oauth_bearer)) -> utils.UserToken:
    try:
        return jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Authentication token invalid')


def encode_user_token(id: int, username: str) -> str:
    token_object = { "id": id, "name": username }
    
    return jwt.encode(token_object, os.getenv('JWT_SECRET'))

def compare_password(password, hashed_password) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

