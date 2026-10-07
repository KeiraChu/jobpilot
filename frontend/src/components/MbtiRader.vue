<template>
    <div class="mbtiradar">
        <div class="chart" ref="chart"></div>
    </div>
</template>

<script>
var option;
export default{
    data(){
        return{
        }
    },
    methods:{
        createChart(){
            var myChart = this.$echarts.init(this.$refs.chart);
        option = {
          tooltip: {
            trigger: 'item'
        },
  title: {
  },
  // legend: {
  //   data: ['类型占比']
  // },
  radar: {
    // shape: 'circle',
    indicator: [
      { name: '外向型', max: 100 },
      { name: '直觉型', max: 100 },
      { name: '感受型', max: 100 },
      { name: '展望型', max: 100 },
      { name: '谨慎型', max: 100 },
    ]
  },
  series: [
    {
      name: '类型占比',
      type: 'radar',
      data: [
        {
          value: [83, 69, 61, 71, 71],
          name: '类型占比',
          label: {
            show: true,
            formatter: function (params) {
              return params.value;
            }
          }
        },
        
      ]
    }
  ]
};
myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });
        }
    },
    mounted(){
        this.$nextTick(() => {  
            this.createChart();  
        });
    }
}
</script>

<style lang="less" scoped>
.chart{
    width: 400px;
    height: 340px;
}
</style>