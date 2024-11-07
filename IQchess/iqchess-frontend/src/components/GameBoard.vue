<template>
  <div class="game-board">
    <h2>Chess Game</h2>
    <div id="chessboard" ref="chessboard"></div>
  </div>
</template>

<script>
import Chessboard from 'chessboardjs';

export default {
  name: 'GameBoard',
  mounted() {
    this.board = Chessboard(this.$refs.chessboard, {
      draggable: true,
      dropOffBoard: 'trash',
      sparePieces: true
    });
  }
};
</script>

<style scoped>
.game-board {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

#chessboard {
  width: 400px;
  height: 400px;
}
</style>