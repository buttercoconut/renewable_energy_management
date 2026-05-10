<template>
  <div class="chart">
    <canvas id="lineChart" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import { Line } from 'chart.js';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const props = defineProps({
  data: { type: Object, required: true },
});

let chartInstance: Line | null = null;

const renderChart = () => {
  const ctx = (document.getElementById('lineChart') as HTMLCanvasElement).getContext('2d');
  if (!ctx) return;
  if (chartInstance) chartInstance.destroy();
  chartInstance = new Line(ctx, {
    data: props.data,
    options: { responsive: true, plugins: { legend: { position: 'top' } } },
  });
};

onMounted(() => renderChart());
watch(() => props.data, renderChart, { deep: true });
</script>
