#-- title: Get User's Articles
#-- description: Code to get all the articles written by a Medium User.
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
user = medium.user(username="nishu-jain")

# Fetch user-written articles
user.fetch_articles()

#%%
# Iterate over user articles and print their title
for article in user.articles:
    print(article.title)