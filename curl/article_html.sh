#-- title: Article's HTML
#-- description: Shell command to retrieve article in plain HTML format.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/article/d9b04a431d7e/html?fullpage=true&style_file=https://mediumapi.com/styles/dark.css"