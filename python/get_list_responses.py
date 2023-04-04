#-- title: Get List Responses
#-- description: Code to get Responses/Comments on a Medium List.
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
# Get the "MediumList" object
medium_list = medium.list(list_id="38f9e0f9bea6")

#%%
# Iterate over medium_list's responses and print their content
for response in medium_list.responses:
    print(response.content)