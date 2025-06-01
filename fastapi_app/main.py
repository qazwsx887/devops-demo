from fastapi import FastAPI, HTTPException

app = FastAPI()

def add(a: float, b: float):
    return a + b

def subtract(a: float, b: float):
    return a - b

def multiply(a: float, b: float):
    return a * b

def divide(a: float, b: float):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

@app.get("/calc")
def calculate(a: float, b: float, operation: str):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation not in operations:
        raise HTTPException(status_code=400, detail="不支持的操作类型")

    try:
        result = operations[operation](a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
