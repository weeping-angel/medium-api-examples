#-- title: Get Recommended Articles
#-- description: Code to get a list of recommended articles for the given Medium Article
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
# Get the "Article" object and fetch recommended articles
article = medium.article(article_id="67fa62fc1971")
article.fetch_recommended_articles()

#%%
# Loop through recommended_articles and print their title and claps count
for article in article.recommended_articles:
    print(f"{article.title} ({article.claps} claps)")