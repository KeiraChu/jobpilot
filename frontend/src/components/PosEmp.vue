<template>
    <div class="posemp">
        <div class="charts" ref="charts"></div>
    </div>
</template>
<script>
export default{
    data(){
        return{
        }
    },
    methods:{
        createChart(){
            var myChart = this.$echarts.init(this.$refs.charts);
    // 2.指定配置
    var option = {
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['职位', '求职人员']
  },
  toolbox: {
    show: true,
    feature: {
      dataView: { show: true, readOnly: false },
      magicType: { show: true, type: ['line', 'bar'] },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  calculable: true,
  xAxis: [
    {
      type: 'category',
      // prettier-ignore
      data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: '职位',
      type: 'bar',
      data: [
        2, 4, 7, 23, 25, 76, 135, 162, 32, 20, 6, 3
      ],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    },
    {
      name: '求职人员',
      type: 'bar',
      data: [
        2, 5, 9, 26, 28, 70, 175, 182, 48, 18, 6, 2
      ],
      markPoint: {
        data: [
          { name: 'Max', value: 182, xAxis: 7, yAxis: 183 },
          { name: 'Min', value: 2, xAxis: 11, yAxis: 3 }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
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

.charts{
    width: 500px;
    height: 350px;
}

</style>