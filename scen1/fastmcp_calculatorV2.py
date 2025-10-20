#libraries
from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool(
    name="multiply",
    description="Multiply two numbers together.",
    tags={"math", "arithmetic"}
)
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    args: a (float): The first number.
          b (float): The second number.

    returns: float: The product of the two numbers.
    
    """
    return a * b

@mcp.tool(
    name="add",
    description="Add two numbers together.",
    tags={"math", "arithmetic"}
)
def add(a: float, b: float) -> float:
    """Add two numbers.

    args: a (float): The first number.
          b (float): The second number.

    returns: float: The sum of the two numbers.

    """
    return a + b

@mcp.tool(
    name="subtract",
    description="Subtract one number from another.",
    tags={"math", "arithmetic"}
)
def subtract(a: float, b: float) -> float:
    """Subtract one number from another.

    args: a (float): The number to subtract from.
          b (float): The number to subtract.

    returns: float: The result of the subtraction.

    """
    return a - b

@mcp.tool(
    name="divide",
    description="Divide one number by another.",
    tags={"math", "arithmetic"}
)
def divide(a: float, b: float) -> float:
    """Divide one number by another.

    args: a (float): The numerator.
          b (float): The denominator.

    returns: float: The result of the division.

    """
    if b == 0:
        return 0
    return a / b

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8003) # Run using HTTP transport