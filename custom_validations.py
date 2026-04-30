from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError("Account ID must be positive")
        return value

def validate_user(user_info:dict):
    try:
        User(**user_info)
        return "User details are valid"
    except ValidationError as e:
        errors = []
        for error in e.errors():
            errors.append(f"{error['loc'][0]}: {error['msg']}")
        return errors
    return None

user_info = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "account_id": 12345}


print(validate_user(user_info))
