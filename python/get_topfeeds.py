#-- title: Get TopFeeds
#-- description: Code to get TopFeed Articles from Medium.
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
# Create a "TopFeeds" Object with mode="new"
topfeeds = medium.topfeeds(tag="blockchain", mode="new")

# Fetch all the articles information
topfeeds.fetch_articles()

#%%
# Iterate over topfeeds articles and print their title
for article in topfeeds.articles:
    print(article.title)
