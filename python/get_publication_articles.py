#-- title: Get Publication Articles
#-- description: Code to get recently published articles on a Medium Publication.
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
# Create a "Publication" Object
publication = medium.publication(publication_id="98111c9905da")

#%%
# Fetch publication articles and print their titles
publication.fetch_articles()

for article in publication.articles:
    print(article.title)