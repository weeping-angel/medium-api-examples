// getLatestPost.js - Fetch the latest posts for a specific topic 

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

// Create an instance of MediumClass with the API key
const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch the latest posts for a specific topic and log the result
medium.getLatestPosts('technology').then(data => {
    console.log('Latest Posts:', data);
});
