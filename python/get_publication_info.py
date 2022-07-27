#-- title: Get Publication Info
#-- description: Code to get a Medium's Publication-related Information.
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
# Print all the properties of the "Publication" object
print('Name: ', publication.name)
print('Tagline: ', publication.tagline)
print('Description: ', publication.description)
print('Followers: ', publication.followers)
print('Tags: ', publication.tags)
print('Slug: ', publication.slug)
print('URL: ', publication.url)

print('Facebook Pagename: ', publication.facebook_pagename)
print('Twitter Username: ', publication.twitter_username)
print('Instagram Username: ', publication.instagram_username)