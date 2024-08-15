#-- title: Get Recommended Users
#-- description: Code to get the recommended users, for the given tag, from Medium Platform
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
# Get the recommended users for the given tag
recommended_users = medium.recommended_users(tag="artificial-intelligence")

#%%
# Print the name and username of each recommended user
recommended_users.fetch_users()

for user in recommended_users.users:
    print(user.fullname, f" ({user.username})")
