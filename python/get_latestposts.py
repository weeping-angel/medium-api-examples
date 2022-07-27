#-- title: Get LatestPosts
#-- description: Code to get LatestPosts for the given topic_slug.
#-- tags: python, medium_api, medium_api_py


# Import libraries
import os
from medium_api import Medium

#%%
# Get RAPIDAPI_KEY from the environment
api_key = os.getenv('RAPIDAPI_KEY')

#%%
# Create a `Medium` Object
medium = Medium(api_key)

#%%
# Create a "LatestPosts" Object
latestposts = medium.latestposts(topic_slug="blockchain")

# Print Length of Post's ID (article_ids)
print(len(latestposts.ids), '\n')

# Fetch information for each article
latestposts.fetch_articles()

#%%
# Iterate over latestposts articles and print their title
for article in latestposts.articles:
    print(article.title)