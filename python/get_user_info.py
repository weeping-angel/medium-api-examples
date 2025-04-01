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
print('Tier: ', user.tier)
print('Profile Image: ', user.image_url)
print('Top Writer In: ', user.top_writer_in)

print('User Written Articles: ', len(user.article_ids))

print('Followers: ', user.followers_count)
print('Following: ', user.following_count)
print('Publication Following: ', user.publication_following_count)

print("Has Lists? : ", user.has_list)
print("Is Book Author? : ", user.is_book_author)
print('Tipping Link: ', user.tipping_link)

print('Is enrolled in writer program: ', user.is_writer_program_enrolled)
print('Became Medium Member At: ', user.medium_member_at)
print('Friend Since: ', user.friend_since)
print('Is Account Suspended? : ', user.is_suspended)
print('Allow Notes? : ', user.allow_notes)

print('Background Image: ', user.bg_image_url)
print('Logo Image: ', user.logo_image_url)

print('Twitter Username: ', user.twitter_username)