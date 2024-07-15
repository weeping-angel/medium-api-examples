#-- title: User Books
#-- description: Shell command to retrieve books published by the given user
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/user/6e2475a6e38a/books"