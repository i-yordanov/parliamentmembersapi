from datetime import date
from pydantic import BaseModel, validator, EmailStr


class PrimeMinisterSchema(BaseModel):
    first_name: str = None
    last_name: str = None
    date_of_birth: date = None
    place_of_birth: str = None
    political_force: str = None
    language1: str = None
    language2: str = None
    language3: str = None
    language4: str = None
    language5: str = None
    email: EmailStr = None
    profession1: str = None
    profession2: str = None
