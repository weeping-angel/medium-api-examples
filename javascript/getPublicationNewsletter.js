// getPublicationNewsletter.js - Fetches newsletter details for a publication

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const publicationId = '98111c9905da'; 

// Fetch the publication newsletter details and log the result
medium.getPublicationNewsletter(publicationId)
    .then(data => {
        console.log('Publication Newsletter:', data);
    })
    
