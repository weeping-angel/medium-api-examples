// getUserTopArticles.js - Fetches the top articles of a user

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '1985b61817c3';

// Fetch the top articles of a user based on their user ID
medium.getUserTopArticles(userId)
    .then(data => console.log('User Top Articles:', data));