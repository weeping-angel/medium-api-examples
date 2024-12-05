// getArticleMarkdown.js - Fetches the Markdown content of a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which Markdown content needs to be fetched
const articleId = '67fa62fc1971'; 

// Fetch the Markdown content of the article and log the response
medium.getArticleMarkdown(articleId).then(data => {
    console.log('Article Markdown:', data);
});
