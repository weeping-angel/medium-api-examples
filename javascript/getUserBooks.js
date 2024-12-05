// getUserBooks.js - Fetches the books associated with a specific user

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '6e2475a6e38a'; 

// Fetch the books associated with the specified user
medium.getUserBooks(userId)
    .then(data => {
        console.log('User Books:', data);
    });
    
