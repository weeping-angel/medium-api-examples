// getArticleResponses.js - Fetches the responses for a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which responses need to be fetched
const articleId = '67fa62fc1971'; 

// Fetch the responses of the article and log the response
medium.getArticleResponses(articleId).then(data => {
    console.log('Article Responses:', data);
});
