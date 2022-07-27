#-- title: Get Article's Responses
#-- description: Code to get Responses/Comments on a Medium Article.
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
# Get the "Article" object and fetch responses
article = medium.article(article_id="67fa62fc1971")

article.fetch_responses()

#%%
# Iterate over article's responses and print their content
for response in article.responses:
    print(response.content)
    print('\n\n---\n\n')