import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

ai = medium.top_writers(topic_slug="artificial-intelligence")

# Top writers count in "artificial-intelligence"
print(len(ai.ids), '\n')

# Fetch information for each top writer
ai.fetch_users()

for writer in ai.users:
    print(writer.fullname, '---', writer.username)