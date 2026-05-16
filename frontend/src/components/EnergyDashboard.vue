<template>
  <div>
    <h2>Energy Dashboard</h2>
    <!-- Placeholder for chart -->
    <canvas id="energyChart"></canvas>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

const chartRef = ref(null)

onMounted(() => {
  const ctx = document.getElementById('energyChart').getContext('2d')
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar'],
      datasets: [{
        label: 'Predicted Power (MW)',
        data: [120, 150, 130],
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    }
  })
})
</script>
<style scoped>
canvas { width: 100%; height: 400px; }
</style>
