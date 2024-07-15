#-- title: Root Tags
#-- description: Shell command to retrieve root (top-level) tags from Medium Platform
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/root_tags"