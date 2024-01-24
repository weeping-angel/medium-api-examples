#-- title: Recommended Articles
#-- description: Shell command to retrieve recommended Medium Articles with respect to the given Article
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/b7d838c84f72/recommended"