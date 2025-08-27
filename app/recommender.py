import requests

def get_recommendations(book_title):
    url = f"https://openlibrary.org/search.json?title={book_title}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error fetching data from OpenLibrary:", response.status_code)
        return []

    try:
        data = response.json()
    except ValueError:
        print("❌ Failed to decode JSON. Response text was:", response.text)
        return []

    if not data.get("docs"):
        return []

    book = data["docs"][0]

    title = book.get("title", "N/A")
    author = book.get("author_name", ["Unknown"])[0]
    cover_id = book.get("cover_i")
    image_url = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else ""
    description = book.get("first_sentence", ["No description available"])[0]
    genre = book.get("subject", ["Unknown"])[0]

    return [{
        "title": title,
        "author": author,
        "genre": genre,
        "description": description,
        "image_url": image_url
    }]
