#-- title: User's Top Articles
#-- description: Shell command to retrieve user's top 10 articles
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \ 
    https://medium2.p.rapidapi.com/user/1985b61817c3/top_articles