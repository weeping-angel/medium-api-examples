// getUserListsById.js - Fetches the lists associated with a user using their user ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '5142451174a3';

// Fetch the lists associated with the user based on their user ID
medium.getUserListsById(userId)
    .then(data => console.log('User Lists:', data));
