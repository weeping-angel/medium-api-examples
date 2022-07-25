import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

article = medium.article(article_id="67fa62fc1971")

article.fetch_responses()

for response in article.responses:
    print(response.content)