# MCP Demo

**Source:** Based on code from the [Hugging Face MCP Course Unit 1: Gradio MCP](https://huggingface.co/learn/mcp-course/unit1/gradio-mcp).

A demo combining Gradio’s MCP integration and the FastMCP SDK to showcase both human-facing interfaces and MCP server capabilities.

## Repository Structure

```
├── letter_counter.py    # Gradio MCP-enabled letter counter demo
├── server.py            # FastMCP-based weather service MCP server
├── main.py              # (Optional entry point / combined launcher)
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Lock file for dependencies
└── notebook.ipynb       # Exploratory notebook (if present)
```

## Features

* **Letter Counter (Gradio MCP)**

  * Counts occurrences of a specified letter in input text.
  * Human-friendly web UI plus MCP tool endpoint via `demo.launch(mcp_server=True)`.

* **Weather Service (FastMCP SDK)**

  * Exposes `get_weather`, `weather_resource`, and `weather_report` as MCP tools, resources, and prompts.
  * Runs as an SSE MCP server on port 3001.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/seanpoyner/mcp_Demo.git
   cd mcp_Demo
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install "gradio[mcp]"
   pip install -r requirements.txt
   ```

*(Requirements should include `gradio[mcp]` and the MCP SDK package, e.g., `modelcontextprotocol`.)*

## Usage

### Letter Counter

1. Launch the Gradio interface and MCP server:

   ```bash
   python letter_counter.py
   ```
2. Access the UI at `http://localhost:7860`.
3. The MCP endpoint is available at:

   ```text
   http://localhost:7860/gradio_api/mcp/sse
   ```

### Weather Service

1. Run the FastMCP server:

   ```bash
   python server.py
   ```
2. The MCP server listens on port 3001 (SSE transport):

   ```text
   http://localhost:3001/gradio_api/mcp/sse
   ```
3. Explore capabilities via the MCP Inspector (if enabled):

   ```text
   http://localhost:6274
   ```

## API Reference

### `letter_counter(word: str, letter: str) -> int`

Count the number of times `letter` appears in `word`.

**Endpoints**:

* Human UI: Gradio textbox inputs → web interface
* MCP tool: `/gradio_api/mcp/sse` → JSON-RPC calls

### FastMCP Weather Tools

```python
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return f"The current weather in {location}: Sunny, 72°F."

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource"""
    return f"The current weather in {location}: Sunny, 72°F."

@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"You are a weather reporter. Please provide a weather report for {location}."
```

## Contributing

Improvements and fixes are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
