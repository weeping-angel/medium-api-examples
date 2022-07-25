import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

# Fetch latest posts
latestposts = medium.latestposts(topic_slug="blockchain")

print(len(latestposts.ids), '\n')

# Fetch information for each article
latestposts.fetch_articles()

for article in latestposts.articles:
    print(article.title)