<template>
  <div class="safety">
    <h2>Safety Incident Report</h2>
    <ul>
      <li v-for="incident in incidents" :key="incident.id">
        {{ incident.date }} - {{ incident.description }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const incidents = ref([]);

onMounted(async () => {
  const res = await axios.get('/api/safety/incidents');
  incidents.value = res.data;
});
</script>

<style scoped>
.safety { padding: 1rem; }
</style>
