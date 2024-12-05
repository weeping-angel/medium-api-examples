// getRelatedTags.js - Fetches related tags for a specific tag

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch related tags for the 'technology' tag
medium.getRelatedTags('technology')
    .then(data => {
        console.log('Related Tags:', data);
    }
)
   
