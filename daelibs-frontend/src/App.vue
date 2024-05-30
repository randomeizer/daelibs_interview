<template>
  <div id="app">
    <h1>Score List</h1>
    <ScoreList :data="data" />
  </div>
</template>

<script>
import { getData } from './services/dataService';
import ScoreList from './components/ScoreList.vue';

export default {
  name: 'App',
  components: {
    ScoreList
  },
  data() {
    return {
      data: []
    };
  },
  created() {
    this.data = getData();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
