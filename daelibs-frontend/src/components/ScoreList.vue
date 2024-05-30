<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Target Score</th>
          <th>Actual Score</th>
          <th>Total Points</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in data" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.target }}%</td>
          <td :style="{ color: item.actual >= item.target ? 'green' : 'red' }">{{ item.actual }}%</td>
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
}

th, td {
  padding: 8px 12px;
  border: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f4f4f4;
}

tr:hover {
  background-color: #f1f1f1;
}
</style>