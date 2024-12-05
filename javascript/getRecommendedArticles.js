// getRecommendedArticles.js - Fetches recommended articles for a given article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const articleId = '67fa62fc1971'; 

// Fetch the recommended articles and log the result
medium.getRecommendedArticles(articleId).then(data => {
    console.log('Recommended Articles:', data);
});
