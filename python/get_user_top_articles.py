#-- title: Get User's Top Articles
#-- description: Code to get top 10 user-written articles on their profile
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
# Create an "User" Object
user = medium.user(username="nishu-jain")

#%%
# Fetch Top Articles and print their title
user.fetch_top_articles()

for article in user.top_articles:
    print(article.title)

# Number of Pinned Articles
print("\nNumber of Pinned Articles: ", user.total_pinned_articles)