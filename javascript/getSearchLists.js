// getSearchLists.js - Fetches search results for lists based on a query

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log list search results
medium.getSearchLists('productivity').then(data => {
    console.log('Search Results for Lists:', data);
});

