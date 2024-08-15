#-- title: Get Root Tags
#-- description: Code to get the root tags (top-level tags) from Medium Platform
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
# Get the root tags
root_tags = medium.root_tags()

#%%
# Print the root tags
for tag in root_tags:
    print(tag)
