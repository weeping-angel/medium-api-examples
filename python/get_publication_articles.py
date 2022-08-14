#-- title: Get Publication Articles
#-- description: Code to get recently published articles on a Medium Publication.
#-- tags: python, medium_api, medium_api_py


# Import libraries
import os
from datetime import datetime, timedelta
from medium_api import Medium

#%%
# Get RAPIDAPI_KEY from the environment
api_key = os.getenv('RAPIDAPI_KEY')

#%%
# Create a `Medium` Object
medium = Medium(api_key)

#%%
# Create a "Publication" Object
publication = medium.publication(publication_id="98111c9905da", save_info=False)


#%%
# Fetch publication articles published within last week's days
last_weeks_articles = publication.get_articles_between(
                                _from=datetime.now(), 
                                _to=datetime.now() - timedelta(days=7)
                            )

for article in last_weeks_articles:
    print(article.title, f'({article.published_at})')