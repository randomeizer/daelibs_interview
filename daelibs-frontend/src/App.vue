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
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');

#app {
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  color: #5A5A5A;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
