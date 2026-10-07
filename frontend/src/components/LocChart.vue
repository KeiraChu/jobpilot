<template>
    <div class="location">
        <h2>热门专业</h2>
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
    var option = {
        color: [
            "#006cff",
            "#60cda0",
            "#ed8884",
            "#ff9f7f",
            "#0096ff",
            "#9fe6b8",
            "#32c5e9",
            "#1d9dff"
        ],
        tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        
        series: [{
            name: "热门专业",
            type: "pie",
            radius: ["10%", "70%"],
            center: ["50%", "50%"],
            roseType: "radius", // 半径模式
            // 图形的文字标签
            label: {
                fontSize: 10
            },
            // 链接图形和文字的线条
            labelLine: {
                // length 链接图形的线条
                length: 6,
                // length2 链接文字的线条
                length2: 8
            },
            data: [{
                    value: 20,
                    name: "软件工程"
                },
                {
                    value: 26,
                    name: "网络工程"
                },
                {
                    value: 24,
                    name: "计算机科学与技术"
                },
                {
                    value: 25,
                    name: "电子科学与技术"
                },
                {
                    value: 20,
                    name: "信息管理与信息系统"
                },
                {
                    value: 25,
                    name: "电子信息科学与技术"
                },
                
            ]
        }]
    };
    myChart.setOption(option);
    // 监听浏览器缩放，图表对象调用缩放resize函数
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
    width: 350px;
    height: 152px;
}
</style>