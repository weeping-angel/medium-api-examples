#-- title: Get Article Fans
#-- description: Code to get a list of users who clapped on Medium Article
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
# Get the "Article" object and fetch fans information
article = medium.article(article_id="67fa62fc1971")
article.fetch_fans()

#%%
# Loop through fans and print their name and username
for fan in article.fans:
    print(f"{fan.fullname} - @{fan.username}")