import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

article = medium.article(article_id="deedea890da1")

print(article.markdown)