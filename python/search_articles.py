#-- title: Search Articles
#-- description: Code to search articles for the given query, on the Medium platform
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
# Search for "startup" related articles
startup_articles = medium.search_articles(
                                    query="startup", 
                                    save_info=True # Warning: Set this True only if you've enough API calls (>1000).
                                )

#%%
# Loop through all the articles and print their title and subtitle
for article in startup_articles:
    print(f"{article.title} - {article.subtitle}")