#-- title: Get Article Info
#-- description: Code to get article-related information
#-- tags: python, medium_api, medium_api_py


# Import libraries
import os
from medium_api import Medium

#%%
# Create `Medium` Object your RAPIDAPI_KEY
medium = Medium(os.environ['RAPIDAPI_KEY'])

#%%
# Get the "Article" object
article = medium.article(article_id="67fa62fc1971")

#%%
# Print article properties
print('Title: ', article.title)
print('Subtitle: ', article.subtitle)
print('AuthorID: ', article.author.user_id)
print('PublicationID: ', article.publication._id)
print('Claps: ', article.claps)
print('Voters: ', article.voters)
print('WordCount: ', article.word_count)
print('ResponseCount: ', article.responses_count)
print('ReadingTime: ', article.reading_time)
print('Tags: ', article.tags)
print('Topics: ', article.topics)
print('TopHighlight: ', article.top_highlight)
print('Language: ', article.lang)
print('PublishedAt: ', article.published_at)
print('LastModifiedAt: ', article.last_modified_at)
print('Responses: ', len(article.response_ids))
print('IsSeries: ', article.is_series)
print('IsLocked: ', article.is_locked)
print('IsShortform: ', article.is_shortform)
print('Image: ', article.image_url)
print('UniqueSlug: ', article.unique_slug)
print('URL: ', article.url)