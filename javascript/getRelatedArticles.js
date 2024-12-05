// getRelatedArticles.js - Fetches related articles for a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const articleId = '67fa62fc1971';

// Fetch related articles for the given articleId
medium.getRelatedArticles(articleId).then(data => {console.log('Related Articles:', data);})
    