#-- title: Recommended Users
#-- description: Shell command to retrieve recommended users (who to follow) for the given tag
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/recommended_users/self-improvement"