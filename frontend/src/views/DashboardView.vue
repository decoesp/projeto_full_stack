<template>
  <div class="dashboard-container">
    <h1 class="text-center">Dashboard</h1>
    <div class="mt-4 mb-4">
      <ChartsDisplay />
    </div>
    <router-link to="/" class="btn btn-primary">Voltar para página inicial</router-link>
  </div>
</template>

<script>
import ChartsDisplay from '@/components/ChartsDisplay.vue';

export default {
  components: {
    ChartsDisplay,
  },
};
</script>

<style>
.dashboard-container {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 50px;
}
.btn {
  line-height: 50px;
  height: 50px;
  text-align: center;
  width: 250px;
  cursor: pointer;
  text-decoration: none;

}
.btn-primary {
  height: 33.33%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  background-color: #66A182;
}


.btn-primary {
  color: #FFF;
  transition: all 0.5s;
  position: relative;
}
.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  background-color: rgba(255,255,255,0.1);
  transition: all 0.3s;
}
.btn-primary:hover::before {
  opacity: 0 ;
  transform: scale(0.5,0.5);
}
.btn-primary::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  opacity: 0;
  transition: all 0.3s;
  border: 1px solid rgba(255,255,255,0.5);
  transform: scale(1.2,1.2);
}
.btn-primary:hover::after {
  opacity: 1;
  transform: scale(1,1);
}
</style>
