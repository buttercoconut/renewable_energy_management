<template>
  <router-view />
</template>

<script setup>
import { createRouter, createWebHistory } from 'vue-router'
import EnergyDashboard from './components/EnergyDashboard.vue'
import MaintenanceSchedule from './components/MaintenanceSchedule.vue'
import SafetyReport from './components/SafetyReport.vue'

const routes = [
  { path: '/', component: EnergyDashboard },
  { path: '/maintenance', component: MaintenanceSchedule },
  { path: '/safety', component: SafetyReport }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
</script>
