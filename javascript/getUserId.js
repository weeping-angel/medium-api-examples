// getUserId.js - Fetches the user ID for a given username (e.g., 'nishu-jain') on Medium

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch the user ID for the specified username
medium.getUserId('nishu-jain')
    .then(data => console.log('User:', data));
