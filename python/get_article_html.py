#-- title: Get Article HTML
#-- description: Code to get Medium Article in plain HTML format.
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
article = medium.article(article_id="9822a049e763")

#%%
# Save the Article's HTML, as full webpage, with css stylesheet, and print it
article.save_html(
    fullpage=True, 
    style_file="https://mediumapi.com/styles/dark.css"
)

print(article.html)