// getArticleAssets.js - Fetches assets for a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which assets need to be fetched
const articleId = '67fa62fc1971'; 

// Fetch assets for the article and log the response
medium.getArticleAssets(articleId).then(data => console.log('Article Assets:', data));