#-- title: User's Publications
#-- description: Shell command to retrieve all the publications where the user is either creator and/or editor.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/user/5142451174a3/publications