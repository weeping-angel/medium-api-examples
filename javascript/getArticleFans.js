// getArticleFans.js - Fetches fans for a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which fans need to be fetched
const articleId = '67fa62fc1971';

// Fetch the fans of the article and log the response
medium.getArticleFans(articleId).then(data => {
    console.log('Article Fans:', data); // Output the fans of the article
});
