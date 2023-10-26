#-- title: Publication's Newsletter
#-- description: Shell command to retrieve newsletter-related information for the given publication.
#-- tags: shell, medium_api, medium_api_curl

curl --header "x-rapidapi-key: $RAPIDAPI_KEY" \
    "https://medium2.p.rapidapi.com/publication/98111c9905da/newsletter"