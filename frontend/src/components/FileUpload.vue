<template>
  <div class="upload-container">
    <label for="fileInput" class="drag-drop-area" @dragover.prevent @dragenter.prevent @dragleave.prevent @drop="handleDrop">
      <p v-if="!file">Arraste e solte arquivos aqui ou clique para fazer o upload.</p>
      <p v-else>Arquivo selecionado: {{ file.name }}</p>
    </label>
    <input type="file" id="fileInput" style="display: none" ref="fileInput" @change="handleFileUpload">
    <p>Arquivos suportados apenas .csv ou .xlsx</p>
    <button class="btn btn-primary" @click="uploadFile">Importar</button>
    <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      metrics: null,
      errorMsg: '',
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
      this.errorMsg = '';
    },
    handleDrop(event) {
      event.preventDefault();
      this.file = event.dataTransfer.files[0];
      this.errorMsg = '';
    },
    uploadFile() {
      if (!this.file) {
        this.errorMsg = 'Selecione um arquivo para fazer o upload.';
        return;
      }

      const allowedExtensions = ['xlsx', 'csv'];
      const fileExtension = this.file.name.split('.').pop().toLowerCase();
      if (!allowedExtensions.includes(fileExtension)) {
        this.errorMsg = 'Formato de arquivo não suportado. Use arquivos .xlsx ou .csv';
        return;
      }

      const formData = new FormData();
      formData.append('file', this.file);

      axios.post('http://localhost:5000/upload', formData)
        .then(response => {
          this.metrics = response.data;
          this.$router.push({ name: 'Dashboard' });
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.drag-drop-area {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  cursor: pointer;
  text-align: center;
  display: block;
}

.drag-drop-area.drag-over {
  background-color: rgba(0, 0, 0, 0.1);
}

.error-msg {
  color: red;
}

.btn {
  line-height: 50px;
  height: 50px;
  text-align: center;
  width: 250px;
  cursor: pointer;
  text-decoration: none;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  background-color: #66A182;
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
  opacity: 0;
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
