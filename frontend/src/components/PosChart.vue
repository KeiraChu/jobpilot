<template>
    <div class="position">
        <h2>热门职位</h2>
        <div class="chart" ref="chart"></div>
    </div>
</template>

<script>
export default{
    data(){
        return{};
    },
    methods:{
        createChart(){
            var myChart = this.$echarts.init(this.$refs.chart);
            var option = {
        color: ["#2f89cf"],
        tooltip: {
            trigger: "axis",
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        // 修改图表的大小
        grid: {
            left: "0%",
            top: "10px",
            right: "0%",
            bottom: "4%",
            containLabel: true
        },
        // x轴
        xAxis: [{
            type: "category",
            data: [
                "前端开发",
                "Java后端开发",
                "网络运维",
                "软件开发",
                "网络工程师",
                "算法工程师",
                "通信工程师",
                "计算机网络维护",
            ],
            axisTick: {
                alignWithLabel: true
            },
            // 修改刻度标签 相关样式
            axisLabel: {
                color: "rgba(255,255,255,.6)",
                fontSize: 10
            },
            // 不显示x坐标轴的样式
            axisLine: {
                show: false
            }
        }],
        // y轴
        yAxis: [{
            type: "value",
            // 修改刻度标签 相关样式
            axisLabel: {
                color: "rgba(255,255,255,.6) ",
                fontSize: 12
            },
            // y轴的线条改为了 2像素
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)",
                    width: 2
                }
            },
            // y轴分割线的颜色
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            }
        }],
        series: [{
            name: "直接访问",
            type: "bar",
            barWidth: "35%",
            data: [1465, 1101, 986, 832, 451, 423, 359],
            itemStyle: {
                // 修改柱子圆角
                barBorderRadius: 5
            }
        }]
    };
    // 3. 把配置项给实例对象
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
    width: 306px;
    height: 152px;
}
</style>