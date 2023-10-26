#-- title: Related Articles
#-- description: Shell command to retrieve articles_ids of the related articles.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/67fa62fc1971/related"