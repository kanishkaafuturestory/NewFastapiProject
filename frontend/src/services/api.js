import axios from 'axios';

const api = axios.create({
    baseURL: '/',  // This will be relative to the current domain
    headers: {
      'Content-Type': 'application/json'
    }
  });
  

export default api;
