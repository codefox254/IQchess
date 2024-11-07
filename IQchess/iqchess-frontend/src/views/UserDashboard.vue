<template>
  <div class="user-dashboard">
    <UserProfile :user="user" />
    <h2>Your Game History</h2>
    <ul>
      <li v-for="game in games" :key="game.id">
        <router-link :to="`/game/${game.id}`">Game against {{ game.chessbot.level }} ({{ game.result }})</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import UserProfile from '../components/UserProfile.vue'; // Update the path

export default {
  name: 'UserDashboard',
  components: {
    UserProfile
  },
  data() {
    return {
      user: {}, // This should be populated with the actual user data
      games: [] // This should be populated with the actual game history data
    };
  }
};
</script>

<style scoped>
.user-dashboard {
  margin-top: 20px;
}

.user-dashboard ul {
  list-style-type: none;
  padding: 0;
}

.user-dashboard li {
  padding: 5px 0;
}
</style>
