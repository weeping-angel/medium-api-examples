#-- title: Search Publication
#-- description: Code to search publications for the given query, on the Medium platform
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
# Search for "artificial intelligence" related publications
ai_pubs = medium.search_publications(
                                    query="artificial intelligence", 
                                    save_info=True # Warning: Set this True only if you've enough API calls (>1000).
                                )

#%%
# Loop through all the publications and print their name and followers
for pub in ai_pubs:
    print(f"{pub.name} - {pub.followers}")