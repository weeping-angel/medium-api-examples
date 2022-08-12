#-- title: Topfeeds
#-- description: Shell command to retrieve the list of topfeed articles for the given "tag" and "mode".
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/topfeeds/ethereum/new