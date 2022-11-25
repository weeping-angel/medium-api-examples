#-- title: Get Related Tags
#-- description: Code to get Related Tags for a given tag
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
# Get related tags for the given tag "blockchain"
related_tags = medium.related_tags(given_tag="blockchain")

#%%
# Iterate and print each related tag
for tag in related_tags:
    print(tag)
