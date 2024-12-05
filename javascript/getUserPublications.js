// getUserPublications.js - Fetches the publications of a user

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '14d5c41e0264'; 

// Fetch the publications of a user based on their user ID
medium.userPublications(userId)
    .then(data => console.log('User Publications:', data));
    