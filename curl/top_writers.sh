#-- title: Top Writers
#-- description: Shell command to retrieve the list of top writers for the given tag/topic_slug.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/top_writers/artificial-intelligence?count=10"