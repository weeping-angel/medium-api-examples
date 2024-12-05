// getRecommendedUsers.js - Fetches recommended users for a specific tag and platform

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);


// Then log the result to the console
medium.getRecommendedUsers('technology').then(data => {
    console.log('Recommended Users:', data);
});
