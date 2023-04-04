#-- title: Get Related Articles
#-- description: Code to get a list of related articles for the given article
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
# Get the "Article" object and fetch related articles
article = medium.article(article_id="67fa62fc1971")
article.fetch_related_articles()

#%%
# Loop through related_articles and print their title and word count
for article in article.related_articles:
    print(f"{article.title} ({article.word_count} words)")