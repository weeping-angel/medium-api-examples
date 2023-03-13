#-- title: Search Articles
#-- description: Shell command to retrieve all the Articles from the Medium Search Results for the given query.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/search/articles?query=startup