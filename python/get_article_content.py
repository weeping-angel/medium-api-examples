#-- title: Get Article's Content
#-- description: To get Medium Article's textual content for given article_id
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
# Get the `Article` object and print its content
article = medium.article(article_id="3134743262d9")
print(article.content)