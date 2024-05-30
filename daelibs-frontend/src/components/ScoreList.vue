<template>
  <div>
    <table>
      <thead>
        <tr>
          <th class="spacer-column spacer-left"></th>
          <th class="name-column">Name</th>
          <th class="spacer-column spacer-right"></th>
          <th class="data-column">Target Score</th>
          <th class="data-column">Actual Score</th>
          <th class="data-column">Total Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in data" :key="index">
          <td class="spacer-column spacer-left"></td>
          <td class="name-column">{{ item.name }}</td>
          <td class="spacer-column spacer-right"></td>
          <td class="data-column">{{ item.target }}%</td>
          <td class="data-column score-cell">
            <div :class="{'score-box': true, 'green': item.actual >= item.target, 'red': item.actual < item.target}">
              {{ item.actual }}%
            </div>
          </td>
          <td class="data-column">{{ item.points }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ScoreList',
  props: {
    data: Array
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');

* {
  font-family: 'Open Sans', sans-serif;
  font-size: 14px;
  color: #5A5A5A;
}

table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}

th, td {
  padding: 8px 12px;
  border: none;
}

thead th {
  background-color: #f8f8f8;
  font-weight: 600;
  text-align: center;
  white-space: nowrap;
  
}

tbody td {
  background-color: #fff;
  border-bottom: 1px solid #ebebeb;
}

tbody tr:hover td {
  background-color: #fbfbfb;
  cursor: pointer;
}

.score-cell {
  display: flex;
  align-items: center;
  justify-content: center;
}

.score-box {
  padding: 4px 8px;
  border-radius: 4px;
  color: white;
  text-align: center;
  font-weight: 700;
  width: 100%;
  max-width: 100px;
}

.green {
  background-color: #59B77A;
}

.red {
  background-color: #ED5E61;
}

/* Common styles for data columns */
.data-column {
  text-align: center;
}

/* Styles for the Name column */
.name-column {
  text-align: left;
  width: 100%;
}

/* Styles for the spacer columns */
.spacer-column {
  width: 52px; /* Default width for left spacer */
}

.spacer-right {
  width: 122px; /* Width for right spacer */
}
</style>