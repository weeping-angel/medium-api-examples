#-- title: Get Archived Articles
#-- description: Code to get the archived articles, for the given tag, from Medium Platform
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
# Get the archived articles for the given tag
archived_articles = medium.archived_articles(
    tag="artificial-intelligence", 
    count=30, 
    year=2023, 
    month=12
)

#%%
# Print the title of each archived article
archived_articles.fetch_articles()

for article in archived_articles.articles:
    print(article.title)
