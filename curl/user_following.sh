#-- title: User's Following
#-- description: Shell command to retrieve user's following
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/user/14d5c41e0264/following