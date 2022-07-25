import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

user = medium.user(username="nishu-jain")

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