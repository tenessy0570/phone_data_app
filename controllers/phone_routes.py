from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import JSONResponse

from dependencies.dependencies import get_phone_data_service
from models.pydantic_models import PhoneDataModel
from services.phone_data_service import PhoneDataService

phone_data_router = APIRouter()


@phone_data_router.get("/check_data")
async def get_phone_data(
        phone: str,
        phone_data_service: Annotated[PhoneDataService, Depends(get_phone_data_service)]
) -> PhoneDataModel:
    result = await phone_data_service.get_data_by_number(phone_number=phone)

    if not result:
        raise HTTPException(status_code=404, detail="Not found")

    return result


@phone_data_router.api_route("/write_data", methods=["POST", "PUT"])
async def set_phone_data(
        phone_data: PhoneDataModel,
        phone_data_service: Annotated[PhoneDataService, Depends(get_phone_data_service)]
):
    await phone_data_service.add_new_phone_data(data=phone_data)
    return JSONResponse(
        {"ok": True},
        status_code=200
    )
