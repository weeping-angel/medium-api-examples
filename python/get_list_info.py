#-- title: Get List Info
#-- description: Code to get Medium's list-related information.
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
medium_list = medium.list(list_id="38f9e0f9bea6", save_info=True)

#%%
# Print Medium List's properties
print('Name: ', medium_list.name)
print('Description: ', medium_list.description)
print('Articles Count: ', medium_list.count)
print('Author ID: ', medium_list.author.user_id)
print('Claps: ', medium_list.claps)
print('Voters/Fans: ', medium_list.voters)
print('Responses Count: ', medium_list.responses_count)
print('Created At: ', medium_list.created_at)
print('Last Item Inserted At: ', medium_list.last_item_inserted_at)
print('Thumbnail: ', medium_list.thumbnail)