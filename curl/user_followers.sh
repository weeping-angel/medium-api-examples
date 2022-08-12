#-- title: User's Followers
#-- description: Shell command to retrieve user's followers
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/user/1985b61817c3/followers