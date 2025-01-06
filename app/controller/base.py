from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from logzero import logger


router = APIRouter()


@router.get('/')
def home():
    try:
        return JSONResponse({'status': status.HTTP_200_OK})
    except Exception as e:
        logger.error('Daily update failed', e)
