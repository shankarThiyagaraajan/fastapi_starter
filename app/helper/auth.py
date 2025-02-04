# ** Base Modules
import os
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
# ** App Modules
from app.models.user import User
from app.service.user import UserService
from app.config import (ALLOWED_AUTH_CLIENT,
                        ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM)
from app.constants import DEFAULT_DATETIME_FORMAT
# ** External Modules
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose.exceptions import JWTError
from typing import Annotated
from jose import jwt

SECRET_KEY = os.getenv('JWT_SECRET_KEY', None)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain, hash) -> bool:
    # Verify the plan and hashed password
    return pwd_context.verify(plain, hash)


def authenticate(email: str, password: str, client: str,
                 with_token=True) -> str | bool:
    """
    Validate and authenticate the user
    Return Newly created token or bool
    Args:
        email (str): Email of the User
        password (str): Plain Password
        client (str): Client of request origin
        with_token (bool, optional): with token or bool

    Returns:
        str | bool: Token or True/False of user authentication
    """
    res = False
    token = None
    us = UserService()
    # Fetch the user by mail
    user = us.get_user(email)
    if user:
        # Verify the user password
        if verify_password(password, user.password):
            res = True
    # Set user if password valid
    user = user if res else None
    # If token included and valid user
    if user and with_token:
        token = create_access_token({'email': email, 'client': client})
        res = token
    # If plain user verifications
    if user:
        res = True
    return res


def is_valid_client(client: str) -> bool:
    # Verify the incoming client with Allowed list
    return client in ALLOWED_AUTH_CLIENT


def create_access_token(data: dict):
    """
    To Create an Access Token

    Args:
        data (dict): {'email': email, 'client_id': client_id}

    Returns:
        _type_: _description_
    """
    expiry = (datetime.now() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).strftime(DEFAULT_DATETIME_FORMAT)
    # Clone the dict
    to_encode = data.copy()
    # add expiry datetime
    to_encode.update({'expiry': expiry})
    # Encrypt the user data to generate token
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)


def get_user_by_token(token: str) -> User:
    if not verify_token(token):
        raise JWTError('Token Expired')
    # Decode the token to extract user data
    data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    us = UserService()
    # Get user by email
    return us.fetch_by_email(data['email'])


def verify_token(token: str) -> bool:
    # User data from token
    data = jwt.decode(token, SECRET_KEY, ALGORITHM)

    expiry = datetime.strptime(data['expiry'], DEFAULT_DATETIME_FORMAT)
    # TODO: Validate Client of the Token and Email
    return expiry >= datetime.now()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        res = get_user_by_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is Expired or Invalid.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Request",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return res


async def get_current_active_user(current_user:
                                  Annotated[User, Depends(get_current_user)]
                                  ) -> User:
    """
    Fetch user by incoming token and verify
    Return: Fetched User
    """
    if not current_user or not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
