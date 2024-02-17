#-- title: Get User's Publication Following
#-- description: Code to get publications that the given user is following.
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
# Create a "User" Object and fetch publication following
user = medium.user(username="nishu-jain")

user.fetch_publication_following()

#%%
# Iterate over user's publication following and print each publication's name
for publication in user.publication_following:
    print(publication.name)