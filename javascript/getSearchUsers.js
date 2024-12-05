// getSearchUsers.js - Fetches search results for users based on a query

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log user search results
medium.getSearchUsers('John Doe').then(data => {
    console.log('Search Results for Users:', data);
});
