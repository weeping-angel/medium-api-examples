// getUserPublicationFollowing.js - Fetches the publications a user is following

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '1985b61817c3'; 

// Fetch the publications that the user is following based on their user ID
medium.getUserPublicationFollowing(userId)
    .then(data => console.log('User Publication Following:', data));
