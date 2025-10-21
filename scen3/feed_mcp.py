from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="FreeCodeCamp Feed Searcher")

@mcp.tool()
def fcc_news_search(query: str, max_results: int = 3):
    """Search news through FreeCodeCamp's RSS feed by title/description"""
    feed = feedparser.parse("https://www.freecodecamp.org/news/rss/")
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = str(entry.get("title", ""))
        description = str(entry.get("description", ""))
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "url": entry.get("link", ""),
            })
        if len(results) >= max_results:
            break
    return results or [{"message": "No results found."}]

if __name__ == "__main__":
    mcp.run()
    