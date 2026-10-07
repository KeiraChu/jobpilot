<template>   
  <div class="knowledge">  
    <div class="chart" ref="chart"></div>  
  </div>  
</template>  
  
<script>  
import Data from '../assets/json/les-miserables.json';
export default {  
  data() {    
    return {    
      graph: null  
    }  
  },  
  methods: {  
    createChart() {  
      const myChart = this.$echarts.init(this.$refs.chart);  
      myChart.showLoading();  
      if (this.graph) { // 确保数据已经加载  
        this.graph.nodes.forEach(node => {  
          node.label = {  
            show: node.symbolSize > 30  
          };  
        });  
          
        // 设置你的 option 对象，这里只是一个示例，你需要根据你的数据来设置  
        const option = {
  title: {
    text: '职位知识图谱',
    subtext: 'Default layout',
    top: 'top',
    left: 'left'
  },
  tooltip: {},
  legend: [
    {
      // selectedMode: 'single',
      data: this.graph.categories.map(function (a) {
        return a.name;
      })
    }
  ],
  animationDuration: 1500,
  animationEasingUpdate: 'quinticInOut',
  series: [
    {
      name: '相应知识图谱',
      type: 'graph',
      layout: 'none',
      data: this.graph.nodes,
      links: this.graph.links,
      categories: this.graph.categories,
      roam: true,
      label: {
        position: 'right',
        // formatter: '{b}'
      },
      force: {
          repulsion: 100
        },
      lineStyle: {
        color: 'source',
        // curveness: 0.3
      },
      emphasis: {
        focus: 'adjacency',
        lineStyle: {
          width: 10
        }
      }
    }
  ]
}; 
          
        myChart.setOption(option);  
        myChart.hideLoading(); // 在设置完 option 后隐藏加载提示  
      }  
        
      window.addEventListener('resize', () => {  
        myChart.resize();  
      });  
    }  
  },  
  mounted() {    
      this.graph=Data;
    this.createChart();  
  }  
}  
</script>  
  
<style scoped>  
.chart{
float: left;
  width: 950px;
  height: 550px;
}
</style>