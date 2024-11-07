<template>
  <div class="game-view">
    <GameBoard />
    <MoveList :moves="moves" />
  </div>
</template>

<script>
import GameBoard from '../components/GameBoard.vue'; // Update the path
import MoveList from '../components/MoveList.vue'; // Update the path

export default {
  name: 'GameView',
  components: {
    GameBoard,
    MoveList
  },
  data() {
    return {
      moves: [] // To be populated with the actual moves data from a chess game
    };
  }
};
</script>

<style scoped>
.game-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}
</style>
