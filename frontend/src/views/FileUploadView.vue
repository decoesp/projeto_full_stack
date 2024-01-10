<template>
  <div class="file-upload-container">
    <div class="card">
      <h1 class="text-center">Importe seu arquivo</h1>
      <p>Carregue uma planilha de dados de seus assinantes.</p>
      <FileUpload />
    </div>
  </div>
</template>

<script>
import FileUpload from '@/components/FileUpload.vue';

export default {
  components: {
    FileUpload
  },
};
</script>

<style>
.file-upload-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f2f2f2;
}

.card {
  background-color: #fff;
  border-radius: 15px;
  padding: 40px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  height: 70%; 
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.card-content {
  text-align: center;
  max-width: 300px;
}

.text-center {
  text-align: center;
}

</style>
