from fastapi import FastAPI

from controllers.phone_routes import phone_data_router

app = FastAPI()
app.include_router(phone_data_router)
