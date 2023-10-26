#-- title: Publication's ID
#-- description: Shell command to retrieve publication_id for the given publication_slug
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/publication/id_for/towards-data-science"