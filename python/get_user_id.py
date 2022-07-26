#-- title: Get User ID
#-- description: Code to retrieve user_id from username
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
# Get the `User` Object using "username" and print ID
user = medium.user(username="nishu-jain")
print(user.user_id)