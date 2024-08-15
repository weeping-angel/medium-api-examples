#-- title: Get Recommended Lists
#-- description: Code to get the recommended lists, for the given tag, from Medium Platform
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
# Get the recommended lists for the given tag
recommended_lists = medium.recommended_lists(tag="artificial-intelligence")

#%%
# Print the recommended lists' names
recommended_lists.fetch_lists()

for lst in recommended_lists.objs:
    print(lst.name)
