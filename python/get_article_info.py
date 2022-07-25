import os
from medium_api import Medium

api_key = os.getenv('RAPIDAPI_KEY')
medium = Medium(api_key)

article = medium.article(article_id="799b2aa6ada3", save_info=True)

print('Title: ', article.title)
print('Subtitle: ', article.subtitle)
print('Author ID: ', article.author.user_id)
print('Publication ID: ', article.publication._id)
print('Claps: ', article.claps)
print('Voters/Fans: ', article.voters)
print('Word Count: ', article.word_count)
print('Reading Time: ', article.reading_time)
print('Tags: ', article.tags)
print('Topics: ', article.topics)
print('Language: ', article.lang)
print('Published At: ', article.published_at)
print('Last Modified At: ', article.last_modified_at)
print('Responses: ', len(article.response_ids))
print('Cover Image: ', article.image_url)
print('URL: ', article.url)