#-- title: List Articles
#-- description: Shell command to retrieve all the articles inside a Medium List
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    https://medium2.p.rapidapi.com/list/38f9e0f9bea6/articles