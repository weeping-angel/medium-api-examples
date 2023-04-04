#-- title: Get Tag Info
#-- description: Code to get the tag-related information from Medium Platform
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
# Get the tag-related information
ai_tag = medium.tag_info(tag="artificial-intelligence")

#%%
# Print the tag-info
print(ai_tag["name"] + '\n')

print("Number of Followers: ", ai_tag["followers"])
print("Number of Stories: ", ai_tag["articles_count"])
print("Number of Latest Stories: ", ai_tag["latest_articles_count"])
print("Number of Writers: ", ai_tag["authors_count"])
print("Number of Latest Writers: ", ai_tag["latest_authors_count"])
