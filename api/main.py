import uvicorn
from fastapi import FastAPI, APIRouter

from api.config import api_config
from api.greeter_api import greeting_router
from api.health_check import health_router

main_api = FastAPI()

main_router = APIRouter(prefix=f'/{api_config.app.version}')
main_router.include_router(health_router)
main_router.include_router(greeting_router)

main_api.include_router(main_router)


def start():
    uvicorn.run(main_api, host='0.0.0.0', port=api_config.app.port)
