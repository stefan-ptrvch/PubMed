<template>
  <div id="app">
    <bar-graph/>
    <br>
    <pie-chart/>
    <br>
    <cities-graph/>
  </div>
</template>

<script>
import BarGraph from './components/BarGraph.vue'
import PieChart from './components/PieChart.vue'
import CitiesGraph from './components/CitiesGraph.vue'

export default {
  name: 'app',
  components: {
    PieChart,
    BarGraph,
    CitiesGraph
  }
}
</script>

<style>
</style>
