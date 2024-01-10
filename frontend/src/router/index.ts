import { createRouter, createWebHistory } from 'vue-router';
import FileUploadView from '@/views/FileUploadView.vue';
import DashboardView from '@/views/DashboardView.vue';

const routes = [
  {
    path: '/',
    name: 'FileUpload',
    component: FileUploadView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
