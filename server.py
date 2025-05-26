from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Weather Service")
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # Simulated response for demonstration purposes
    return f"The current weather in {location}: Sunny, 72°F."
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide the weather data as a resource"""
    return f"The current weather in {location}: Sunny, 72°F."
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    # Simulated response for demonstration purposes
    return f"You are a weather reporter. Please provide a weather report for {location}."
if __name__ == "__main__":
    mcp.run(transport="sse", port=3001)