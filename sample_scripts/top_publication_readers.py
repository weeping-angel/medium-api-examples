# Import required libraries
import os
from collections import Counter
from medium_api import Medium
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pprint import pprint

#%%
# Create a Medium Object
medium = Medium(os.getenv('RAPIDAPI_KEY'))

#%%
# Create a publication Object
publication = medium.publication("37e36bc3e578", save_info=False)

#%%
# Fetch publication articles for the last 30 days
publication_articles = publication.get_articles_between(
                                            _from = datetime.now(), 
                                            _to = datetime.now() - timedelta(days=30)
                                    )

print("Total Articles", len(set(publication_articles)))
print("Latest Article: ", publication_articles[0].published_at)
print("Oldest Article: ", publication_articles[-1].published_at)

#%%
# Filter articles that have responses on them
articles_with_responses = [article for article in publication_articles if article.responses_count!=0]
print('Articles with responses: ', len(articles_with_responses))

#%%
# Retrieve all the responders from all the comments from all the filtered articles
responders = []
for article in articles_with_responses:
    print(article.title, '---', article.responses_count)
    article.fetch_responses()
    for response in article.responses:
        responder = response.author
        responder.save_info()
        print('  - ',responder.username)
        responders.append(responder.username)

results = Counter(responders)
pprint(results)

#%%
# Plotting histogram of the results
plt.bar(results.keys(), results.values())
plt.xlabel(xlabel="username")
plt.xticks(rotation=90)
plt.show()
