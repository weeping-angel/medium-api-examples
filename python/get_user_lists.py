#-- title: Get User's Lists
#-- description: Code to get an array of Medium Lists created by the user.
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
# Fetch User's List-related info and print their names and number of articles
user.fetch_lists()
for user_list in user.lists:
    print(f"{user_list.name} - {user_list.count}")