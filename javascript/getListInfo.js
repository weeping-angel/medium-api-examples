// getListInfo.js - Fetches details of a specific list by its ID

import Medium from 'medium-api-js';
import dotenv from 'dotenv';

dotenv.config();

const medium = new Medium(process.env.RAPIDAPI_KEY);

// Fetch information about a specific Medium list
medium.getListInfo('3d8f744f5370').then(data => {
    console.log('List Info:', data);
});
