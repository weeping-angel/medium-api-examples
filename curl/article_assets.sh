#-- title: Article Assets
#-- description: Shell command to retrieve assets present in a Medium Article
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/b7d838c84f72/assets"