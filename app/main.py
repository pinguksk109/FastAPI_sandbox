from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from response.error_response import ErrorResponse
from controller.usage_controller import router as usage_router

app = FastAPI()

@app.middleware("http")
async def api_key_validator(request: Request, call_next):

    api_key = request.headers.get("X-API-Key")
    if api_key is None or api_key == 'x-api-key':
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    try:
        response = await call_next(request)
    except Exception as e:
        raise HTTPException(status_code=200, detail="Internal Server Error") from e

    return response

app.include_router(usage_router)