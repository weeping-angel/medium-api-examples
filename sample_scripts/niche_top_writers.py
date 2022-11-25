# Import required libraries
import os
from datetime import datetime
from medium_api import Medium

#%%
# Create a Medium Object
medium = Medium(os.getenv('RAPIDAPI_KEY'))

#%%
# Set the niche tag
niche_tag = "blockchain"

# Fetch Top Writers for the niche_tag
niche_top_writers = medium.top_writers(niche_tag).users

#%%
# Fetch related tags for the given niche_tag
related_tags = medium.related_tags(niche_tag)

# Fetch Top Writers for each corresponding related niche tag
for tag in related_tags:
    print(f'- Getting Top Writers for "{tag}"')
    top_writers = medium.top_writers(tag)
    niche_top_writers += top_writers.users

#%%
# Removing redundant top writers
niche_top_writers = set(niche_top_writers)

# Fetch all user-related information
medium.fetch_users(niche_top_writers)

#%%
# Preapre CSV records
csv_header = 'Fullname, Username, UserID\n'
csv_records = ''
for writer in niche_top_writers:
    csv_records += f'"{writer.fullname}", {writer.username}, {writer._id}\n'

# Save the records in CSV file
csv_filename = f'niche_top_writers-{datetime.now(): %d-%b-%Y}'
csv_output = csv_header + csv_records

with open(csv_filename, 'w') as f:
    f.write(csv_output)