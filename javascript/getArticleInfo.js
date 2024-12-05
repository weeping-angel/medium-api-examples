// getArticleInfo.js - Fetches detailed information about a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which information needs to be fetched
const articleId = '67fa62fc1971'; 

// Fetch the detailed information about the article and log the response
medium.getArticleInfo(articleId).then(data => {
    console.log('Article Info:', data);
});
