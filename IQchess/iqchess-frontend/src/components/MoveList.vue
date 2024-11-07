<template>
  <div class="move-list">
    <h2>Move List</h2>
    <ul>
      <li v-for="(move, index) in moves" :key="index">
        {{ index + 1 }}. {{ move }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'MoveList',
  props: {
    moves: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.move-list {
  margin-top: 20px;
}

.move-list ul {
  list-style-type: none;
  padding: 0;
}

.move-list li {
  padding: 5px 0;
}
</style>