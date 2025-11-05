from pathlib import Path
import scrapy
from urllib.parse import urlparse

class YarnSpider(scrapy.Spider):
    name = "yarns"
    
    start_urls = [
        "https://novita.com/collections/langat",
    ]
            
    def parse(self, response, **kwargs):
        parts = [p for p in urlparse(response.url).path.split("/") if p]
        page = parts[-1] if parts else "index"
        filename = f"yarns-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")