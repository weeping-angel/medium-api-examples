// getUserInfo.js - Fetches detailed information about a user using their user ID (e.g., '1985b61817c3')

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch detailed user information for the specified user ID
medium.getUserInfo('1985b61817c3')
    .then(data => console.log('User Info:', data));
