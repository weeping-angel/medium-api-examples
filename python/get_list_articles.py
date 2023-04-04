#-- title: Get List Articles
#-- description: Code to get all the articles within a Medium List
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
# Create an "MediumList" Object
medium_list = medium.list(list_id="38f9e0f9bea6")

# Fetch all the List articles
medium_list.fetch_articles()

#%%
# Iterate over List articles and print their title
for article in medium_list.articles:
    print(article.title)