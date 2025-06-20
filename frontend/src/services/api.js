import axios from 'axios';

const api = axios.create({
  baseURL: '/api', // This will hit FastAPI via Vite proxy
  headers: {
    'Content-Type': 'application/json'
  }
});

export default api;
