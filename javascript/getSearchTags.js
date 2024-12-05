// getSearchTags.js - Fetches search results for tags based on a query

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log tag search results
medium.getSearchTags('coding').then(data => {
    console.log('Search Results for Tags:', data);
});
