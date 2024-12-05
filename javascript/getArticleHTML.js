// getArticleHTML.js - Fetches the HTML content of a specific article

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the article ID for which HTML content needs to be fetched
const articleId = '67fa62fc1971'; 

// Set the parameters for full_page and style_file
const fullPage = true;  // Set to true if you want the full page
const styleFile = "dark.css"; // Set the css file name if you want to include the style file

// Fetch the HTML content of the article and log the response
medium.getArticleHTML(articleId, fullPage, styleFile)
    .then(data => {
        console.log('Article HTML:', data);
    })