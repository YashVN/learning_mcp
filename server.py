from mcp.server import MCPServer

#MCP Server 
mcp = MCPServer("hello-mcp")

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
'''
if __name__ == "__main__":
    mcp.run()'''