// getRecommendedLists.js - Fetches recommended lists for a specific tag

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const tag = 'technology'; 

// Fetch the recommended lists for a specific tag
medium.getRecommendedLists(tag)
    .then(data =>{
     console.log('Recommended Lists:', data)
    }
) 
    
