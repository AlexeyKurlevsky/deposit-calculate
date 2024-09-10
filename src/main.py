from logging import getLogger

import uvicorn
from fastapi import FastAPI

from api import routes
from config import PORT
from utils import init_logger


init_logger()

logger = getLogger(__name__)


def init_app() -> FastAPI:
    app = FastAPI(root_path="/app")
    app.include_router(routes.routes)
    return app


if __name__ == "__main__":
    uvicorn.run(init_app, port=PORT, host="0.0.0.0")
