#-- title: LatestPosts
#-- description: Shell command to retrieve latestposts for the given topic_slug.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/latestposts/blockchain