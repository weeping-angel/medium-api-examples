// getUserFollowers.js - Fetches the followers of a user based on their user ID
import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

const userId = '14d5c41e0264';
const count = 20; 
let after = ""; 

medium.getUserFollowers(userId, count, after)
    .then(data => {
        console.log('User Followers:', data);
    });