import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

publication = medium.publication(publication_id="98111c9905da")

print('Name: ', publication.name)
print('Tagline: ', publication.tagline)
print('Description: ', publication.description)
print('Followers: ', publication.followers)
print('Tags: ', publication.tags)
print('Slug: ', publication.slug)
print('URL: ', publication.url)

# Social profiles
print('Facebook Pagename: ', publication.facebook_pagename)
print('Twitter Username: ', publication.twitter_username)
print('Instagram Username: ', publication.instagram_username)