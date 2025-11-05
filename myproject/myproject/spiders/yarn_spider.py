from pathlib import Path
import scrapy
from urllib.parse import urlparse

class YarnSpider(scrapy.Spider):
    name = "yarns"
    
    # Use Scrapy's standard entry point: either define `start_urls` or `start_requests` (sync)
    start_urls = [
        "https://novita.com/collections/langat",
    ]
            
    def parse(self, response, **kwargs):
        # Build a stable filename from the last path segment (handles URLs with/without trailing slash)
        parts = [p for p in urlparse(response.url).path.split("/") if p]
        page = parts[-1] if parts else "index"
        filename = f"yarns-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")