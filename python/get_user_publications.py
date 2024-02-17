#-- title: Get User's Publications
#-- description: Code to get a list of Medium Publications where the user is either editor and/or creator.
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
user = medium.user(username="zulie")

#%%
# Fetch User's Publication-related info and print their names
user.fetch_publications()

print(f'{user.fullname} is admin in following publications: \n')
for user_pub in user.publications['admin_in']:
    print(user_pub.name)

print(f'\n{user.fullname} is contributing writer in following publications: \n')
for user_pub in user.publications['writer_in']:
    print(user_pub.name)