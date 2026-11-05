from mcp.server import MCPServer


#MCP Server 
mcp = MCPServer("Calculator",
                instructions = "Simple Calculator")

@mcp.tool()
def add(a:int, b:int) -> int:
    ''' Adds two numbers together.
     a : integer
     b : integer
    return : integer'''
    return a + b

@mcp.tool()
def subtract(a:int, b:int) -> int:
    ''' Subtracts two numbers.
     a : integer
     b : integer
    return : integer'''
    return a - b

@mcp.tool()
def multiply(a:int, b:int) -> int:
    ''' Multiplies two numbers together.
     a : integer
     b : integer
    return : integer'''
    return a * b

@mcp.tool()
def divide(a:int, b:int) -> float:
    ''' Divides two numbers.
     a : integer
     b : integer
    return : float'''
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.tool()
def modulus(a:int, b:int) -> int:
    ''' Returns the modulus of two numbers.
     a : integer
     b : integer
    return : integer'''
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b


@mcp.resource("calc://constants")
def constants() -> str:
    """
    Returns a string representation of some mathematical constants.
    """
    return (
        "pi = 3.14\n"
        "e = 2.718\n"
        "1 inch = 2.54cm\n"
    )
@mcp.resource("calc://table/{number}")
def table(number:int)->str:
    return "\n".join(f"{number} x {i} = {number*i}" for i in range(1,11))

app = mcp.streamable_http_app()

if __name__ == "__main__":
    mcp.run('stdio')