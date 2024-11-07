import { createStore } from 'vuex';
import axios from 'axios';

// Define mutation types as constants
const SET_USER_PROFILE = 'SET_USER_PROFILE';
const SET_CURRENT_GAME = 'SET_CURRENT_GAME';
const SET_GAME_MOVES = 'SET_GAME_MOVES';
const SET_ANALYSIS = 'SET_ANALYSIS';

export default createStore({
  state: {
    userProfile: null,
    currentGame: null,
    gameMoves: [],
    analysis: null,
  },
  mutations: {
    [SET_USER_PROFILE](state, profile) {
      state.userProfile = profile;
    },
    [SET_CURRENT_GAME](state, game) {
      state.currentGame = game;
    },
    [SET_GAME_MOVES](state, moves) {
      state.gameMoves = moves;
    },
    [SET_ANALYSIS](state, analysis) {
      state.analysis = analysis;
    },
  },
  actions: {
    async fetchUserProfile({ commit }) {
      try {
        const response = await axios.get('/api/userprofile/');
        commit(SET_USER_PROFILE, response.data);
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    },
    async fetchCurrentGame({ commit }, gameId) {
      try {
        const response = await axios.get(`/api/games/${gameId}/`);
        commit(SET_CURRENT_GAME, response.data);
      } catch (error) {
        console.error('Error fetching current game:', error);
      }
    },
    async fetchGameMoves({ commit }, gameId) {
      try {
        const response = await axios.get(`/api/games/${gameId}/moves/`);
        commit(SET_GAME_MOVES, response.data);
      } catch (error) {
        console.error('Error fetching game moves:', error);
      }
    },
    async fetchAnalysis({ commit }, gameId) {
      try {
        const response = await axios.get(`/api/games/${gameId}/analysis/`);
        commit(SET_ANALYSIS, response.data);
      } catch (error) {
        console.error('Error fetching analysis:', error);
      }
    },
  },
  getters: {
    userProfile: (state) => state.userProfile,
    currentGame: (state) => state.currentGame,
    gameMoves: (state) => state.gameMoves,
    analysis: (state) => state.analysis,
  },
});