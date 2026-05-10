<template>
  <div class="dashboard">
    <h2>Energy Production Forecast</h2>
    <LineChart :data="forecastData" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import LineChart from './LineChart.vue';

const forecastData = ref(null);

onMounted(async () => {
  const res = await axios.get('/api/energy/forecast');
  forecastData.value = res.data;
});
</script>

<style scoped>
.dashboard { padding: 1rem; }
</style>
