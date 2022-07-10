from fastapi import APIRouter

health_router = APIRouter(prefix='/health', tags=['health_checks'])


@health_router.get('', status_code=200)
def is_ok():
    return 'Ok'
