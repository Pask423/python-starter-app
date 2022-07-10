from fastapi import APIRouter

from api.config import api_config

greeting_router = APIRouter(tags=['greet'])


@greeting_router.get('/greet/{name}', status_code=200)
def say_hello(name: str):
    return api_config.app.greet_message + name
