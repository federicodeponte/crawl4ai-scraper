# openpull

Pull structured data from any website using LLM-powered extraction.

Built on [crawl4ai](https://github.com/unclecode/crawl4ai) + Google Gemini.

## Features

- **Pull data from any website** - handles JavaScript-rendered pages
- **LLM-powered extraction** - describe what you want in plain English
- **Structured output** - get clean JSON with optional schema validation
- **Multi-page discovery** - automatically finds and scrapes relevant pages
- **Link extraction** - get internal/external links from any page

## Installation

```bash
pip install openpull
```

Or install from source:

```bash
git clone https://github.com/federicodeponte/openpull.git
cd openpull
pip install -e .
```

### Prerequisites

```bash
playwright install chromium
```

## Quick Start

```python
import asyncio
from openpull import FlexibleScraper

async def main():
    scraper = FlexibleScraper(api_key="your-gemini-api-key")

    result = await scraper.scrape(
        url="https://example.com",
        prompt="Extract the main heading and description",
    )
    print(result)

asyncio.run(main())
```

## Examples

### Basic Extraction

```python
result = await scraper.scrape(
    url="https://company.com",
    prompt="Extract company name, tagline, and main products",
)
# {'company_name': 'Acme Inc', 'tagline': '...', 'products': [...]}
```

### With JSON Schema

```python
schema = {
    "type": "object",
    "properties": {
        "team_members": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "linkedin": {"type": "string"},
                },
            },
        },
    },
}

result = await scraper.scrape(
    url="https://company.com/about",
    prompt="Find all team members with their roles and LinkedIn URLs",
    schema=schema,
)
```

### Multi-Page Discovery

Automatically discover and scrape relevant pages:

```python
result = await scraper.scrape(
    url="https://company.com",
    prompt="Find all team members",
    auto_discover_pages=True,
    max_pages=5,
)
# Scrapes homepage, then uses LLM to find relevant pages like /about, /team
```

### Link Extraction Only

```python
result = await scraper.scrape(
    url="https://news.ycombinator.com",
    prompt="",
    extract_links=True,
)
# {'links': [...], 'internal_links': [...], 'external_links': [...], 'total_links': 123}
```

## API Reference

### `FlexibleScraper(api_key: str)`

Initialize with your Gemini API key.

### `scrape(url, prompt, **kwargs) -> dict`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | str | required | URL to scrape |
| `prompt` | str | required | What to extract (plain English) |
| `schema` | dict | None | JSON schema for structured output |
| `max_pages` | int | 1 | Max pages to scrape |
| `timeout` | int | 30 | Request timeout in seconds |
| `extract_links` | bool | False | Only extract links, skip LLM |
| `auto_discover_pages` | bool | False | Auto-discover relevant pages |

## Environment Variables

```bash
GEMINI_API_KEY=your-api-key-here
```

## Development

```bash
git clone https://github.com/federicodeponte/openpull.git
cd openpull
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

MIT - see [LICENSE](LICENSE)

## Credits

- [crawl4ai](https://github.com/unclecode/crawl4ai) - async web crawler
- [Google Gemini](https://ai.google.dev/) - LLM extraction
- [Playwright](https://playwright.dev/) - browser automation
