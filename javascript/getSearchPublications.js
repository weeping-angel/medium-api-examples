// getSearchPublications.js - Fetches search results for publications based on a query

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log publication search results
medium.getSearchPublications('Tech News').then(data => {
    console.log('Search Results for Publications:', data);
});
