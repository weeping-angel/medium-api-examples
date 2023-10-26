#-- title: Publication's Articles
#-- description: Shell command to retrieve top 25 articles from a publication.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/publication/98111c9905da/articles?from=2023-01-31T13:10:00"