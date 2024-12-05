// getTopFeeds.js - Fetches the top feeds for a specific tag and mode

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch the top feeds for the 'data-science' tag and 'NEW' mode
medium.getTopFeeds('data-science', 'NEW')
    .then(data => {
     console.log('Top Feeds:', data);
    });
