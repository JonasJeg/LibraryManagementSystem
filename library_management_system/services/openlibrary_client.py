from typing import List

import requests


class OpenLibraryClient:
    BASE_URL = "https://openlibrary.org/search.json"

    def search_books(self, query: str, limit: int = 5) -> List[dict]:
        params = {"q": query, "limit": limit}
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            results = []
            for doc in data.get("docs", [])[:limit]:
                title = doc.get("title") or "Unknown title"
                authors = doc.get("author_name") or ["Unknown author"]
                year = doc.get("first_publish_year")
                results.append({
                    "title": title,
                    "author": ", ".join(authors),
                    "year": year
                })
            return results
        except Exception as e:
            print(f"Error contacting OpenLibrary: {e}")
            return []
