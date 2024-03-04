#-- title: Get Recommended Feed
#-- description: Code to get Recommended Feed Articles from Medium.
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
# Create a "RecommendedFeed" Object for the given tag
recommended_feed = medium.recommended_feed(
                tag = "artificial-intelligence",
                count = 15
            )

# Fetch all the articles information
recommended_feed.fetch_articles()

#%%
# Iterate over recommended_feed articles and print their title
for article in recommended_feed.articles:
    print(article.title)
