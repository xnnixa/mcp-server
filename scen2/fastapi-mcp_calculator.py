#HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1 Let's make a FastAPI app (that means API) first

app = FastAPI(title="MCP Calculator API")

@app.post("/multiply")
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers.
    
    args: a (float): The first number.
          b (float): The second number.

    returns: float: The product of the two numbers.
    
    """
    return a * b

@app.post("/add")
def add_numbers(a: float, b: float) -> float:
    """Add two numbers.

    args: a (float): The first number.
          b (float): The second number.

    returns: float: The sum of the two numbers.

    """
    return a + b

@app.post("/subtract")
def subtract_numbers(a: float, b: float) -> float:
    """Subtract one number from another.

    args: a (float): The number to subtract from.
          b (float): The number to subtract.

    returns: float: The result of the subtraction.

    """
    return a - b

@app.post("/divide")
def divide_numbers(a: float, b: float) -> float:
    """Divide one number by another.

    args: a (float): The dividend.
          b (float): The divisor.

    returns: float: The result of the division.

    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#2. Converting it to MCP
mcp = FastApiMCP(app, name="MCP Calculator", description="A calculator API with MCP tools.")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)