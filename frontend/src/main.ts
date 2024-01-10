import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Certifique-se de estar importando corretamente o seu router

const app = createApp(App);

app.use(router);

app.mount('#app');
