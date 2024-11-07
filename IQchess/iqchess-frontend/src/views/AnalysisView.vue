<template>
  <div class="analysis-view">
    <h2>Game Analysis</h2>
    <div v-for="(analysis, index) in analyses" :key="index" class="analysis-item">
      <p><strong>Move {{ index + 1 }}:</strong> {{ analysis.move }}</p>
      <p><strong>Feedback:</strong> {{ analysis.feedback }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnalysisView',
  props: {
    analyses: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.analysis-view {
  margin-top: 20px;
}

.analysis-item {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}
</style>