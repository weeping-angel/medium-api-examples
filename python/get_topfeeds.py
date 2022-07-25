import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

topfeeds = medium.topfeeds(tag="relationships", mode="new")

topfeeds.fetch_articles()

for article in topfeeds.articles:
    print(article.title)