// getTopWriters.js - Fetches the top writers for a specific topic

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Specify the topic and the number of top writers you want to fetch
const topic = 'technology';
const count = 10;

// Fetch the top writers for the specified topic and count
medium.getTopWriters(topic, count)
    .then(data => {
        console.log('Top Writers:', data);
    })