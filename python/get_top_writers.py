#-- title: Get Top Writers
#-- description: Code to get Medium's Top Writers for a given topic_slug/tag.
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
# Create a "TopWriters" Object
ai = medium.top_writers(
        topic_slug="artificial-intelligence",
        count = 10
    )

#%%
# Fetch top writers and print their 'fullname' and 'username'
ai.fetch_users()

for writer in ai.users:
    print(writer.fullname, '---', writer.username)