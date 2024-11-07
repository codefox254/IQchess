import axios from 'axios';

const API_URL = process.env.VUE_APP_API_BASE_URL;

export default {
  getUserProfile(userId) {
    return axios.get(`${API_URL}userprofiles/${userId}/`);
  },
  updateUserProfile(userId, data) {
    return axios.put(`${API_URL}userprofiles/${userId}/`, data);
  },
  getCurrentGame(gameId) {
    return axios.get(`${API_URL}games/${gameId}/`);
  },
  getGameMoves(gameId) {
    return axios.get(`${API_URL}games/${gameId}/moves/`);
  },
  getAnalysis(gameId) {
    return axios.get(`${API_URL}games/${gameId}/analysis/`);
  },
  createGame(data) {
    return axios.post(`${API_URL}games/`, data);
  },
  createMove(gameId, data) {
    return axios.post(`${API_URL}games/${gameId}/moves/`, data);
  },
  createAnalysis(gameId, data) {
    return axios.post(`${API_URL}games/${gameId}/analysis/`, data);
  },
};