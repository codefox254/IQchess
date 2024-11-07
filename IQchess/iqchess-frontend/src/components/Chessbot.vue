<template>
  <div class="chessbot">
    <h2>Select Chessbot Level</h2>
    <div class="chessbot-levels">
      <button v-for="level in levels" :key="level" @click="selectLevel(level)">
        {{ level }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Chessbot',
  data() {
    return {
      levels: ['Easy', 'Medium', 'Hard']
    };
  },
  methods: {
    selectLevel(level) {
      this.$emit('level-selected', level);
    }
  }
};
</script>

<style scoped>
.chessbot {
  margin-top: 20px;
}

.chessbot-levels {
  display: flex;
  justify-content: space-around;
}

.chessbot-levels button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.chessbot-levels button:hover {
  background-color: #0056b3;
}
</style>