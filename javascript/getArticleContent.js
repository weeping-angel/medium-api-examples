// getArticleContent.js - Fetches content for a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which content needs to be fetched
const articleId = '67fa62fc1971';

// Fetch the content of the article and log the response
medium.getArticleContent(articleId).then(data => {
    console.log('Article Content:', data);
});
