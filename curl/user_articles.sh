#-- title: User's Articles
#-- description: Shell command to retrieve user-written articles
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/user/e680fcaf274b/articles?next=1691502178198"