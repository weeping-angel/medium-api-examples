#-- title: Recommended Feed
#-- description: Shell command to retrieve the list of recommended articles for the given "tag".
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/recommended_feed/artificial-intelligence?page=1"