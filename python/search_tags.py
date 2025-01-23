#-- title: Search Tags
#-- description: Code to search similar tags for the given query, on the Medium platform
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
# Search for "blockchain" related users
blockchain_tags = medium.search_tags(query="blockchain")

#%%
# Loop through all the tags
for tag in blockchain_tags:
    print(tag)