import uvicorn
from fastapi import FastAPI

app = FastAPI()

RESULT = 0
OPERATIONS = list()

@app.get("/sum/")
async def lang(a: int = 0, b: int = 0):
    return {"sum": a+b}

@app.get("/dif")
async def dif(a: int = 0, b: int = 0):
        return {"dif": a-b}

@app. get ("/mul")
async def mul(a: int = 0, b: int = 0):
    return {"mul": a*b}

@app.get("/div")
async def div(a: int = 0, b: int = 0):
    return {"div": a/b}

@app.get("/polish")
async def div(op: str, a: int = 0):
    global RESULT

    if op == "+":
        RESULT += a
    elif op == "-":
        RESULT -= a
    elif op == "*":
        RESULT *= a
    elif op == "/" and a > 0:
        RESULT /= a
    else:
        return {"error": f"operation {op} not suported"}
    OPERATIONS.append(f"{op} {a}")

@app.get("/polish_op")
async def div(op: str, a: int = 0):
    return {"op": OPERATIONS}


if __name__ == "__main__":
    uvicorn.run(
        "main: app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )