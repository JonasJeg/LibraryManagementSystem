from unittest.mock import patch
from library_management_system.services.openlibrary_client import OpenLibraryClient

@patch("requests.get")
def test_openlibrary_success(mock_get):
    mock_get.return_value.json.return_value = {
        "docs": [
            {"title": "Book", "author_name": ["Author"], "first_publish_year": 2000}
        ]
    }
    mock_get.return_value.raise_for_status.return_value = None

    client = OpenLibraryClient()
    results = client.search_books("test")

    assert len(results) == 1
    assert results[0]["title"] == "Book"

@patch("requests.get", side_effect=Exception("Network error"))
def test_openlibrary_network_error_returns_empty_list(_):
    client = OpenLibraryClient()
    results = client.search_books("test")
    assert results == []
