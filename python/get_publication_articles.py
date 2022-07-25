import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

publication = medium.publication(publication_id="98111c9905da")

publication.fetch_articles()

for article in publication.articles:
    print(article.title)