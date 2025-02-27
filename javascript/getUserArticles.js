// getUserArticles.js - Fetches articles associated with a specific user

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);


const userId = '6e2475a6e38a'; 

// Fetch the articles associated with the specified 
medium.getUserArticles(userId)
    .then(data => {
        console.log('User Articles:', data);
    });