#-- title: Get Publication Newsletter
#-- description: Code to get newsletter-related information for the given publication
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
# Fetch Newsletter Info and Print Newsletter Info
publication.newsletter.save_info()

print("ID: ", publication.newsletter.id)
print("Name: ", publication.newsletter.name)
print("Description: ", publication.newsletter.description)
print("Slug: ", publication.newsletter.slug)
print("Subscribers: ", publication.newsletter.subscribers)
print("Image URL: ", publication.newsletter.image_url)