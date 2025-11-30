"""openpull: Pull structured data from any website using LLM extraction."""

from .scraper import FlexibleScraper, FlexibleScraperError

__version__ = "0.1.0"
__all__ = ["FlexibleScraper", "FlexibleScraperError"]
