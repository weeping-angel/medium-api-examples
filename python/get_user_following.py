#-- title: Get User's Following
#-- description: Code to get a User's following.
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
# Create a "User" Object and fetch followings
user = medium.user(username="seanjkernan")

user.fetch_following()

#%%
# Iterate over user following and print their fullname
for person in user.following:
    print(person.fullname)