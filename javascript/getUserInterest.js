// getUserInterests.js - Fetches the list of interests for a user using their user ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '1985b61817c3';

// Fetch the interests of the user based on their user ID
medium.getUserInterests(userId)
    .then(data => console.log('User Interests:', data));
