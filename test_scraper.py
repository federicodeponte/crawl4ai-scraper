"""Quick test of the scraper."""

import asyncio
import os
from dotenv import load_dotenv
from scraper import FlexibleScraper

load_dotenv()


async def test():
    api_key = os.getenv("GEMINI_API_KEY")
    print(f"API Key loaded: {'Yes' if api_key else 'No'}")

    scraper = FlexibleScraper(api_key)
    print("Scraper initialized successfully")

    print("\nTesting scrape on https://example.com...")
    result = await scraper.scrape(
        url="https://example.com",
        prompt="Extract the main heading and any paragraph text",
    )
    print(f"Result: {result}")
    print("\nTest passed!")


if __name__ == "__main__":
    asyncio.run(test())
