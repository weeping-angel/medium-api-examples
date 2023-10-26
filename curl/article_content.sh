#-- title: Article's Content
#-- description: Shell command to retrieve Article's Textual Content.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/562c5821b5f0/content"