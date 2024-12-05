// getSearchArticles.js - Fetches search results for articles based on a query

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log article search results
medium.getSearchArticles('technology').then(data => {
    console.log('Search Results for Articles:', data);
});
