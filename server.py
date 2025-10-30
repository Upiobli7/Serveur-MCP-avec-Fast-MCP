from fastmcp import FastMCP

# Créer le serveur
mcp = FastMCP("Test Technique HexaDone")

# TOOLS 
@mcp.tool()
def addition(a: float, b: float) -> float:
    """Additionne deux nombres"""
    return a + b


@mcp.tool()
def multiplication(a: float, b: float) -> float:
    """Multiplie deux nombres"""
    return a * b


@mcp.tool()
def dire_bonjour(nom: str = "Monde") -> str:
    """Dit bonjour à quelqu'un"""
    return f"Bonjour {nom} ! "

# RESOURCE 

@mcp.resource("config://version")
def get_version() -> str:
    """Version du serveur"""
    return "1.0.0"

if __name__ == "__main__":
    mcp.run(transport="sse", port=8000, host="0.0.0.0")
