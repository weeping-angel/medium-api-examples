#-- title: Recommended Lists
#-- description: Shell command to retrieve recommended lists for the given tag
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/recommended_lists/self-improvement"