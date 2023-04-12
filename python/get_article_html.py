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
article = medium.article(article_id="ff6369938b63")

#%%
# Save the Article's HTML, as full webpage and print it
article.save_html(fullpage=True)

print(article.html)