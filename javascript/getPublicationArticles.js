// getPublicationArticles.js - Fetches articles associated with a specific publication

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);
const publicationId = '98111c9905da'; 
const from = '2023-01-31T13:10:00';  // Set the starting point for fetching articles

// Fetch the articles associated with the publication and log the response
medium.getPublicationArticles(publicationId, from)
    .then(data => {
        console.log('Publication Articles:', data);
    })