// getListArticles.js - Fetches articles in a specific list by its ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch and log articles from a specific list
medium.getListArticles('3d8f744f5370').then(data => {
    console.log('List Articles:', data);
});