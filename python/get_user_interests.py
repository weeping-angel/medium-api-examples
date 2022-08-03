#-- title: Get User's Interest
#-- description: Code to get a list of tags followed by a user.
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
# Create an "User" Object
user = medium.user(username="nishu-jain")

#%%
# Print users interests
for interest in user.interests:
    print(interest)