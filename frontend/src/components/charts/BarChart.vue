<template>

    <Bar :chart-data="chartData" 
    :options="chartOptions"
    :style="myStyles" />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  computed: {
    myStyles () {
      return {
        height: `${10}px`,
        position: 'relative'
      }
    }
  },
  data() {
    return {
      chartData: {
        labels: [ 'Игорь', 'Артем', 'Жора'],
        datasets: [
          {
            label: 'Уровень тупости',
            backgroundColor: '#ba4949',
            data: [40, 20, 12]
          }
        ]
      },
      chartOptions: {
        responsive: true
      }   
    }
  }
}
</script>