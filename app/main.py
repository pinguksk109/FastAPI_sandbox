from fastapi import FastAPI
from controllers import zipcode_controller

app = FastAPI()

app.include_router(zipcode_controller.router)