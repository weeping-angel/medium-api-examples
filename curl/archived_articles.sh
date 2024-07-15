#-- title: Archived Articles
#-- description: Shell command to retrieve archived Medium Articles for the given tag
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/archived_articles/self-improvement?year=2023&month=6"