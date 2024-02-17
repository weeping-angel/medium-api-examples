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
article = medium.article(article_id="67fa62fc1971")

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
print('Top Highlight: ', article.top_highlight)
print('Language: ', article.lang)
print('Published At: ', article.published_at)
print('Last Modified At: ', article.last_modified_at)
print('Responses: ', len(article.response_ids))
print('Is Series: ', article.is_series)
print('Is Locked: ', article.is_locked)
print('Is Shortform: ', article.is_shortform)
print('Cover Image: ', article.image_url)
print('Unique Slug: ', article.unique_slug)
print('URL: ', article.url)