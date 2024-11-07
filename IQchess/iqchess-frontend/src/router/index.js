import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue'; // Ensure this matches the file name (HomeView.vue)
import GameView from '../views/GameView.vue';
import UserDashboard from '../views/UserDashboard.vue';
import AnalysisView from '../views/AnalysisView.vue';

Vue.use(VueRouter);

// Define routes
const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path: '/game',
    name: 'GameView',
    component: GameView,
  },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
  },
  {
    path: '/analysis',
    name: 'AnalysisView',
    component: AnalysisView,
  },
];

// Create and configure router
const router = new VueRouter({
  mode: 'history', // Use the HTML5 history mode
  base: process.env.BASE_URL, // Base URL for the application
  routes,
});

export default router;
