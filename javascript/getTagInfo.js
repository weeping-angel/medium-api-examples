// getTagInfo.js - Fetches detailed information about a specific tag

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch information about a specific tag, in this case, 'technology'
medium.getTagInfo('technology')
    .then(data => {
        console.log('Tag Info:', data);
    });
    
