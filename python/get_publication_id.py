#-- title: Get Publication ID
#-- description: Code to retrieve publication_id for the given publication_slug
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
# Get the `Publication` Object using "publication_slug" and print ID
publication = medium.publication(publication_slug="towards-data-science")
print(publication._id)