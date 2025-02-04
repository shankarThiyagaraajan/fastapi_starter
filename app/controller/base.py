from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.helper.auth import (
    authenticate, get_current_active_user, create_access_token)
from app.pyd_models import Token
from logzero import logger
from typing import Annotated


router = APIRouter()


@router.get('/')
def home():
    try:
        return JSONResponse({'status': status.HTTP_200_OK})
    except Exception as e:
        logger.error('Daily update failed', e)


@router.post('/token')
def new_rule(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    if authenticate(form_data.username, form_data.password, 'web'):
        data = {'email': form_data.username}
        access_token = create_access_token(data)
        return Token(access_token=access_token, token_type="bearer")
    else:
        return JSONResponse({'error': 'Authentcation Failed'},
                            status.HTTP_401_UNAUTHORIZED)


@router.get('/user')
def get_user(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
