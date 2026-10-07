<template>
    <div class="radar">
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
  color: ['#67F9D8', '#FFE434', '#56A3F1', '#FF917C'],
  tooltip: {
            trigger: 'item'
        },
  title: {
    text: ''
  },
  legend: {},
  radar: [
    {
      indicator: [
        { text: '学历' , max: 100},
        { text: '工作经历', max: 100 },
        { text: '期望城市', max: 100 },
        { text: '薪资', max: 100 },
        { text: '专业技能', max: 100 },
        { text:'项目经历', max: 100}
      ],
      center: ['50%', '50%'],
      radius: 120,
      startAngle: 90,
      splitNumber: 4,
      // shape: 'circle',
      axisName: {
        formatter: '【{value}】',
        color: '#428BD4'
      },
      splitArea: {
        areaStyle: {
          color: ['#77EADF', '#26C3BE', '#64AFE9', '#428BD4'],
          shadowColor: 'rgba(0, 0, 0, 0.2)',
          shadowBlur: 10
        }
      },
      axisLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      },
      splitLine: {
        lineStyle: {
          color: 'rgba(211, 253, 250, 0.8)'
        }
      }
    },
  ],
  series: [
    {
      type: 'radar',
      emphasis: {
        lineStyle: {
          width: 4
        }
      },
      data: [
        {
          value: [67, 78,80, 80, 76,87],
          name: '求职者平均水平'
        },
        {
          value: [60, 80, 67, 56, 70,83],
          name: '你的条件',
          areaStyle: {
            color: 'rgba(255, 228, 52, 0.6)'
          }
        }
      ]
    },
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
    text-align: center;
    width: 750px;
    height: 340px;
}
</style>