// getRecommendedFeed.js - Fetches the recommended feed for a specific tag and page

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the tag and the page number for the recommended feed
const tag = 'technology';
const page = 2; 

// Fetch the recommended feed for the specified tag and page number
medium.getRecommendedFeed(tag, page)
    .then(data => {
        console.log('Recommended Feed:', data);
    })

