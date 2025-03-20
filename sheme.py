from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, EmailStr
from datetime import date
import json
import os

app = FastAPI()

class Subscriber(BaseModel):
    surname: constr(regex=r'^[А-ЯЁ][а-яё]+$')
    name: constr(regex=r'^[А-ЯЁ][а-яё]+$')
    birth_date: date                           
    phone_number: constr(regex=r'^\+?[0-9]{10,15}$')  
    email: EmailStr                            

@app.post("/submit/")
async def submit_subscriber(subscriber: Subscriber):
    data = subscriber.dict()
    file_path = "subscribers.json"
    
   
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    existing_data.append(data)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

    return {"message": "Subscriber data saved successfully", "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
