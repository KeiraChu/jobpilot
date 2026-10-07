<template>  
    <div class="edu">
      <h2>职位学历要求</h2>
      <div class="chart" ref="chart"></div>
    </div>
  </template>  

  <script>

  export default {
      data() {  
        return {  
          }
        },
        methods:{
          createChart(){
            var myChart = this.$echarts.init(this.$refs.chart);
            var option={
tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center',
    textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: "12"
            }
  },
  series: [
    {
      name: '数量',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center',
        color:'#fff'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '40',
          fontWeight: 'bold',
          color:'#fff'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 1714, name: '本科' },
        { value: 462, name: '硕士' },
        { value: 150, name: '博士' },
        { value: 386, name: '专科及以下' }
      ]
    }
  ]
            };
            myChart.setOption(option);
            // 监听浏览器缩放，图表对象调用缩放resize函数
            window.addEventListener("resize", function() {
              myChart.resize();
            });
          }
        },
        mounted() {  
        this.$nextTick(() => {  
              this.createChart();  
          });
      }
      }

</script>

<style lang="less" scoped>
.chart{
  width: 350px;
  height: 152px;
}
</style>