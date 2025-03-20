from datetime import date

from pydantic import BaseModel, field_validator, model_validator, Field, EmailStr
from typing import Annotated


class Person(BaseModel):
    id: int = Field(default=1, description="unque id", )
    name: str = Field(
        default="firs_name_last_name",
        min_length=10,
        man_length=100
    ) 
    b_date: date = Field(default="2000-01-01", title="brithday day")
    email: str = Field(pattern=r"[^@]+@utmn.ru", description="e-mail")

class Student(Person):
    score: int = Field(
        default=80,
        ge=80,
        le=300
        )
    
    
class Postgraduate(Person): 
    grant: int = Field(ge=1000, le=10000)
    


class CarProperty(BaseModel):
    id: int = Field(default=1, description="unque id")
    name: str = Field(default="auto")
    value: str = Field(default="auto")


class Car(BaseModel):
    id: Annotated[int, Field(default=1, description="unque id")]
    # id: int = Field(default=1, description="unque id")
    brand: str = Field(default="auto")
    propertes: list[CarProperty]


if __name__ == "__main__":
    p1 = CarProperty(id=1, name="max_speed", value="200")
    p2 = CarProperty(id=2, name="color", value="black")
    p3 = CarProperty(id=3, name="clereance", value="220")

    myCar = Car(id=1, brand="Toyota", propertes=[p1, p2, p3])


    print(myCar.model_dump())