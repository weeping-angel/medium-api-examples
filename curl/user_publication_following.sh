#-- title: User Publication Following
#-- description: Shell command to retrieve publications that the give user is following
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/user/1985b61817c3/publication_following"