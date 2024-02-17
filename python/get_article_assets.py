#-- title: Get Article's Assets
#-- description: Code to get assets present in the Medium Article such as images, videos, embeds, etc ...
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
# Get the "Article" object
article = medium.article(article_id="b7d838c84f72")


#%%
# Print URLs of all the images that are present in the article
for image_url in article.assets.images:
    print(image_url)

# Print URLs of all the YouTube videos that are present in the article
for video in article.assets.youtube:
    print(video['href'])

# Print URLs of all the GitHub Gists that are present in the article
for gist_url in article.assets.github_gists:
    print(gist_url)