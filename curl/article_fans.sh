#-- title: Article's Fans
#-- description: Shell command to retrieve user_ids of the people who clapped on the article.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/67fa62fc1971/fans"