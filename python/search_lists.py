#-- title: Search Lists
#-- description: Code to search Lists for the given query, on the Medium platform
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
# Search for "tech" related Lists
tech_lists = medium.search_lists(
                                query="technology", 
                                save_info=True # Warning: Set this True only if you've enough API calls (>1000).
                                )

#%%
# Loop through all the Lists and print their name, id and article's count
for lst in tech_lists:
    if lst.name is not None:
        print(f"{lst.name} - {lst._id} - {lst.count}")