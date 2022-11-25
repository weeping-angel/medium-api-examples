# Import required libraries
import os
import markdown
from medium_api import Medium

#%%
# Create a Medium Object
medium = Medium(os.getenv('RAPIDAPI_KEY'))

#%%
# Get an Article object
article_url = "https://pub.towardsai.net/why-its-super-hard-to-be-an-ml-researcher-or-developer-67fa62fc1971"
article_id = medium.extract_article_id(article_url)

article = medium.article(article_id)

#%%
# Convert Markdown to HTML
html_output = markdown.markdown(article.markdown)

#%%
# Save the HTML
with open('index.html', 'w', encoding='utf-8') as f:
    html_output = html_output.replace('’', "'")
    f.write(html_output)