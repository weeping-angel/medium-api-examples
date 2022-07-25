import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

article = medium.article(article_id="3134743262d9")

print(article.content)