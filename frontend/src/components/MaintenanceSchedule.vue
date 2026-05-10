<template>
  <div class="maintenance">
    <h2>Maintenance Schedule</h2>
    <ul>
      <li v-for="item in schedule" :key="item.id">
        {{ item.date }} - {{ item.task }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const schedule = ref([]);

onMounted(async () => {
  const res = await axios.get('/api/maintenance/schedule');
  schedule.value = res.data;
});
</script>

<style scoped>
.maintenance { padding: 1rem; }
</style>
