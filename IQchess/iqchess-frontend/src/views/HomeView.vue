<template>
  <div class="home-view">
    <h1>Welcome to the Chess Application</h1>
    <p>Play against our AI-powered chessbot, analyze your games, and improve your skills!</p>
    <router-link to="/game" class="btn">Start a Game</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
};
</script>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 50px;
  padding: 0 20px;
}

h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
}

p {
  font-size: 1.2rem;
  color: #555;
  max-width: 600px;
  line-height: 1.6;
  margin-bottom: 30px;
}

.btn {
  display: inline-block;
  padding: 12px 24px;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  text-decoration: none;
  margin-top: 20px;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn:hover {
  background-color: #0056b3;
  transform: translateY(-3px); /* Adds a subtle lift on hover */
}
</style>
