// getListResponses.js - Fetches responses to a specific list by its ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch responses/comments on a specific list
medium.getListResponses('3d8f744f5370').then(data => {
    console.log('List Responses:', data);
});
