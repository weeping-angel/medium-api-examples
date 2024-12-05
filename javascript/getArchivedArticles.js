// getArchivedArticles.js - Fetches Archived Articles for a specific tag

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

let tag = 'technology'; 
let year = 2023;
let month = 6; 
let next = "";  

// Fetch archived articles with the specified parameters
medium.getArchivedArticles(tag, year, month, next).then(data => {
    console.log('Archived Articles:', data);
})

