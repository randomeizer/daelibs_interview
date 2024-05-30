<!-- src/components/ScoreList.vue -->
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th nowrap>Target&nbsp;Score</th>
          <th nowrap>Actual&nbsp;Score</th>
          <th nowrap>Total&nbsp;Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in data" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.target }}%</td>
          <td>
            <div :class="{'score-box': true, 'green': item.actual >= item.target, 'red': item.actual < item.target}">
              {{ item.actual }}%
            </div>
          </td>
          <td>{{ item.points }}</td>
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
table {
  width: 100%;
  border-collapse: collapse;
  table-layout: auto;
}

th, td {
  padding: 8px 12px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

th:first-child {
  width: 100%; /* Allow the Name column to stretch */
}

tr:hover {
  background-color: #f1f1f1;
}

.score-box {
  padding: 4px 8px;
  border-radius: 12px;
  color: white;
  display: inline-block;
}

.green {
  background-color: green;
}

.red {
  background-color: red;
}
</style>