#-- title: Get Article Markdown
#-- description: Code to get Article in Markdown format.
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
# Get the "Article" object and print markdown
article = medium.article(article_id="deedea890da1")
print(article.markdown)