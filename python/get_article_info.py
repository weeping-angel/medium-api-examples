#-- title: Get Article Info
#-- description: Code to get article-related information.
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
# Get the "Article" object
article = medium.article(article_id="799b2aa6ada3", save_info=True)

#%%
# Print article properties
print('Title: ', article.title)
print('Subtitle: ', article.subtitle)
print('Author ID: ', article.author.user_id)
print('Publication ID: ', article.publication._id)
print('Claps: ', article.claps)
print('Voters/Fans: ', article.voters)
print('Word Count: ', article.word_count)
print('Responses Count: ', article.responses_count)
print('Reading Time: ', article.reading_time)
print('Tags: ', article.tags)
print('Topics: ', article.topics)
print('Language: ', article.lang)
print('Published At: ', article.published_at)
print('Last Modified At: ', article.last_modified_at)
print('Responses: ', len(article.response_ids))
print('Cover Image: ', article.image_url)
print('URL: ', article.url)