<template>
    <div class="percent">
        <div class="chart" ref="chart"></div>  
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
            var myChart = this.$echarts.init(this.$refs.chart);
    // 2.指定配置
    var option = {
      tooltip: {
            trigger: "axis",
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
            }
        },
  dataset: {
    source: [
      ['score', 'amount', 'product'],
      [89.3, 58212, '专业技能'],
      [57.1, 78254, '教育经历'],
      [74.4, 41032, '工作经历'],
      [50.1, 12755, '期望薪资'],
      [89.7, 20145, '期望城市'],
      [68.1, 79146, '项目经历'],
      [70.6, 91852, '期望职位']
    ]
  },
  grid: { 
    containLabel: true,
    left: '2%',
    top: '2%', 
  },
  xAxis: { name: '%' },
  yAxis: { type: 'category' },
  visualMap: {
    orient: 'horizontal',
    left: 'center',
    min: 10,
    max: 100,
    text: ['非常适合', '不适合'],
    // Map the score column to color
    dimension: 0,
    inRange: {
      color: [ '#ECF7FC','#8BB8E7', '#0a65cc']
    }
  },
  series: [
    {
      type: 'bar',
      encode: {
        // Map the "amount" column to X axis.
        x: 'percent',
        // Map the "product" column to Y axis
        y: 'product'
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

.chart{
  float: left; 
    width: 750px;
    height: 450px;
    margin: 0;
    padding: 0;
}

</style>