#-- title: Get User Info
#-- description: Code to get Medium User's Information
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
# Print all the attributes of the Medium User
print('Fullname: ', user.fullname)
print('Bio: ', user.bio)
print('Profile Image: ', user.image_url)

print('User Written Articles: ', len(user.article_ids))

print('Followers: ', user.followers_count)
print('Following: ', user.following_count)

print('Is enrolled in writer program: ', user.is_writer_program_enrolled)
print('Became Medium Member At: ', user.medium_member_at)
print('Is Account Suspended? : ', user.is_suspended)
print('Allow Notes? : ', user.allow_notes)

print('Twitter Username: ', user.twitter_username)