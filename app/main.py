from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from response.error_response import ErrorResponse
from controller.usage_controller import router as usage_router

app = FastAPI()

@app.middleware("http")
async def api_key_validator(request: Request, call_next):
    x_api_key = request.headers.get("X-API-Key")
    if not x_api_key or x_api_key != "x-api-key":  # Replace with actual validation logic
        # HTTPExceptionを発生させる
        raise HTTPException(status_code=401, detail="Invalid or missing X-API-Key")
    
    response = await call_next(request)
    return response

app.include_router(usage_router)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    # 標準のHTTPExceptionを使用してエラーレスポンスを返す
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )