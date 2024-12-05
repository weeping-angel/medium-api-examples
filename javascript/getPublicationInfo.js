// getPublicationInfo.js - Fetches detailed information about a publication

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const publicationId = '98111c9905da';

// Fetch the detailed information of the publication and log the result
medium.getPublicationInfo(publicationId)
    .then(data => {
        console.log('Publication Info:', data);
    })
   