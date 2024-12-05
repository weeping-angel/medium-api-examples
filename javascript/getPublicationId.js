// getPublicationId.js - Fetches the publication ID for a given publication slug

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const publicationSlug = 'codex'; 

// Fetch the publication ID for the given slug and log the response
medium.getPublicationId(publicationSlug).then(data => {
    console.log('Publication ID:', data);
});
