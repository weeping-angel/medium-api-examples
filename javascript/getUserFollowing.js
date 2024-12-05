// getUserFollowing.js - Fetches the users that a specific user is following based on their user ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '14d5c41e0264'; 

// Fetch the users that the specified user is following
medium.getUserFollowing(userId)
    .then(data => console.log('User Following:', data))

