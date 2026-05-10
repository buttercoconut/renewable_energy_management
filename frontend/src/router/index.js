import { createRouter, createWebHistory } from 'vue-router';
import EnergyDashboard from '../components/EnergyDashboard.vue';
import MaintenanceSchedule from '../components/MaintenanceSchedule.vue';
import SafetyReport from '../components/SafetyReport.vue';

const routes = [
  { path: '/', component: EnergyDashboard },
  { path: '/maintenance', component: MaintenanceSchedule },
  { path: '/safety', component: SafetyReport },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
