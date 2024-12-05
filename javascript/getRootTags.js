// getRootTags.js - Fetches the root tags available on the Medium platform

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch root tags available on the Medium platform
medium.getRootTags()
    .then(data => {
     console.log('Root Tags:', data);
    }
)
    