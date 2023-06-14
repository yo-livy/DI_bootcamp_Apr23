import os
import django
import requests
from book_review_app.models import Book
from dateutil import parser


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_top.settings')
django.setup()


def populate_books_from_api():
    # Make a request to the Google Books API
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=search_term')

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        counter = 0  # Counter for limiting the number of books processed

        # Loop through the retrieved books
        for item in data['items']:
            if counter >= 200:
                break  # Stop processing books once the limit is reached

            volume_info = item['volumeInfo']

            # Extract relevant information
            title = volume_info['title']
            author = volume_info['authors'][0] if 'authors' in volume_info else 'Unknown'
            published_date = volume_info['publishedDate'] if 'publishedDate' in volume_info else None
            
            try:
                parsed_date = parser.parse(published_date).date().isoformat()
            except (TypeError, ValueError):
                parsed_date = None

            description = volume_info['description'] if 'description' in volume_info else ''
            page_count = volume_info['pageCount'] if 'pageCount' in volume_info else 0
            categories = ', '.join(volume_info['categories']) if 'categories' in volume_info else ''
            thumbnail_url = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else ''

            # Create a new book instance and save it
            book = Book(
                title=title,
                author=author,
                published_date=parsed_date,
                description=description,
                page_count=page_count,
                categories=categories,
                thumbnail_url=thumbnail_url
            )
            book.save()

            print("Data added", counter)

            counter += 1  # Increment the counter for each processed book
    else:
        print('Error occurred while retrieving data from the API.')


populate_books_from_api()
