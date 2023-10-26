#-- title: Get User's Followers
#-- description: Code to get a user's followers.
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
# Create an "User" Object and fetch followers
user = medium.user(username="nishu-jain")

user.fetch_all_followers()

#%%
# Iterate over user followers and print their fullname
for follower in user.all_followers:
    print(follower.fullname)