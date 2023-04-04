#-- title: Search Users
#-- description: Code to search users for the given query, on the Medium platform
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
# Search for "data scientist" related users
data_scientists = medium.search_users(
                                    query="data scientist", 
                                    save_info=True # Warning: Set this True only if you've enough API calls (>1000).
                                )

#%%
# Loop through all the users and print their name, username and bio
for user in data_scientists:
    print(f"{user.fullname} (@{user.username}) - {user.bio}")