import asyncio
from fastmcp import Client


async def main():
    # Se connecter au serveur
    async with Client("http://localhost:8000/sse") as client:

        # Appeler addition
        result = await client.call_tool("addition", {"a": 5, "b": 3})
        print(f"5 + 3 = {result.content[0].text}")

        # Appeler multiplication
        result = await client.call_tool("multiplication", {"a": 4, "b": 7})
        print(f"4 × 7 = {result.content[0].text}")

        # Appeler dire_bonjour
        result = await client.call_tool("dire_bonjour", {"nom": "Urbain"})
        print(result.content[0].text)


        # Lire la resource version
        version = await client.read_resource("config://version")
        print(f"Version: {version[0]}")


if __name__ == "__main__":
    asyncio.run(main())
