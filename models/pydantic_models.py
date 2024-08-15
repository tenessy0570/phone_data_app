from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo


class PhoneDataModel(BaseModel):
    number: str
    address: str

    """
    If we require specific phone format, add validation below
    """

    @field_validator("number")
    @classmethod
    def check_phone_format(cls, v: str, info: ValidationInfo) -> str:
        ...
        return v
