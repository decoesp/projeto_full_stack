<template>
  <div>
    <div class="card">
      <div class="card-body">
        <canvas ref="mrrChartCanvas"></canvas>
      </div>
    </div>
    <div class="card">
      <div class="card-body">
        <canvas ref="churnRateChartCanvas"></canvas>
      </div>
    </div>
    <h1>Explicações</h1>
    <div v-for="(explanation, key) in explanations" :key="key">
      <p><strong>{{ key }}:</strong> {{ explanation }}</p>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      explanations: {
        Ativos: 'Usuários ativos na plataforma',
        Cancelamentos: 'Usuários que cancelaram a assinatura',
        Cancelado: 'Usuários que já foram ativos e agora o status é cancelado'
      },
    };
  },
  mounted() {
    axios.get('http://localhost:5000/dados_mrr_churn')
      .then(response => {
        const data = response.data;
        console.log(data);

        // MRR Data
        const mrrMonth = Object.keys(data.MRR).map(month => {
          return `${month}`;
        });

        const mrrValues = Object.keys(data.MRR).map(month => data.MRR[month].MRR);

        // MRR Chart
        new Chart(this.$refs.mrrChartCanvas.getContext('2d'), {
          type: 'line',
          data: {
            labels: mrrMonth,
            datasets: [{
              label: 'MRR',
              data: mrrValues,
              fill: false,
              borderColor: 'blue',
              tension: 0.1
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              tooltip: {
                callbacks: {
                  label: function(context) {
                    const mrrData = data.MRR[mrrMonth[context.dataIndex]];
                    return `${mrrMonth[context.dataIndex]} - MRR: ${mrrData.MRR} - Ativos: ${mrrData.ativos}`;
                  }
                }
              }
            }
          }
        });

        // Churn Rate Data
        const churnRateLabels = Object.keys(data.ChurnRate).map(month => {
          return `${month}`;
        });

        const churnRateValues = Object.keys(data.ChurnRate).map(month => data.ChurnRate[month].churn_rate);

        // Churn Rate Chart
        new Chart(this.$refs.churnRateChartCanvas.getContext('2d'), {
          type: 'line',
          data: {
            labels: churnRateLabels,
            datasets: [{
              label: 'Churn Rate',
              data: churnRateValues,
              fill: false,
              borderColor: 'red',
              tension: 0.1
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              tooltip: {
                callbacks: {
                  label: function(context) {
                    const churnData = data.ChurnRate[churnRateLabels[context.dataIndex]];
                    return `${churnRateLabels[context.dataIndex]} - Churn Rate: ${churnData.churn_rate}% - Ativos: ${churnData.ativos}, Cancelamentos: ${churnData.cancelamentos}, Cancelado: ${churnData.cancelados}`;
                  }
                }
              }
            }
          }
        });
      })
      .catch(error => {
        console.error(error);
      });
  },
};
</script>

<style>
.card {
  padding: 0px 200px 0px 200px;
}

.card-body {
  width: 100%;
  margin-bottom: 40px;
}
</style>
