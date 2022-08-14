# Import required libraries
import os
from collections import Counter
from medium_api import Medium
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from itertools import takewhile

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

print("Total Articles: ", len(set(publication_articles)), '\n')
print("Latest Article: ", publication_articles[0].published_at)
print("Oldest Article: ", publication_articles[-1].published_at)

#%%
# Filter articles that have responses on them
articles_with_responses = [article for article in publication_articles if article.responses_count!=0]
print('\nArticles with responses: ', len(articles_with_responses), '\n')

#%%
# Retrieve all the responders from all the comments from all the filtered articles
authors = []
for article in articles_with_responses:
    print('>>> ', article.title)
    article.fetch_responses()
    authors += [response.author for response in article.responses]

medium.fetch_users(authors)
responders = [author.username for author in authors]

results = Counter(responders)

most_comments_num = results.most_common(1)[0][1]
top_commenters = [i[0] for i in takewhile(lambda x: x[1]==most_comments_num, results.most_common())]


print(f"\nNumber of people who commented on Articles: {len(results)}")
print(f"Total number of comments: {len(responders)}")
print(f"People who commented the most ({most_comments_num} times): {', '.join(top_commenters)}")
#%%
# Plotting histogram of the results
plt.bar(results.keys(), results.values())
plt.xlabel(xlabel="username")
plt.xticks(rotation=45)
plt.show()
