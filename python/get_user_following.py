import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

user = medium.user(username="zulie")

for person in user.following:
    print(person.fullname)