from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers.api.v1 import router as api_v1_router
from app.exceptions.resource_not_found import ResourceNotFoundException

def create_app():
    app = FastAPI()

    @app.exception_handler(ResourceNotFoundException)
    async def resource_not_found_handler(_request: Request, _exc: ResourceNotFoundException):
      return JSONResponse(
        status_code=404,
        content={"message": f"Oops! Seems like what you are looking for does not exist."},
      )
    
    app.include_router(api_v1_router, prefix="/api/v1")
    
    return app

