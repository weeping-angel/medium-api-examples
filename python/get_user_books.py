#-- title: Get User's Books
#-- description: Code to get all the books published by a verified Medium User.
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
# Create an "User" Object using 'username'
user = medium.user(username="anangsha")

#%%
# Iterate over books and print their details
for book in user.books:
    print("Name: ", book.name)
    print("Description: ", book.description)
    print("Authors: ", book.authors)
    print("URLs: ", book.urls)
    print("Published On: ", book.published_on)
    print("Cover Image: ", book.cover)

    print('\n')