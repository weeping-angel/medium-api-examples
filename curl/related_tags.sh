#-- title: Related Tags
#-- description: Shell command to retrieve related tags for the given tag.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/related_tags/blockchain"