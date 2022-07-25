import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

user = medium.user(username="nishu-jain")

user.fetch_top_articles()

for article in user.top_articles:
    print(article.title)