<template>
    <div class="employee">
        <h2>求职人数变化
                    <!-- 年份数据切换 -->
                    <!-- <a href="javascript:;">2022</a> -->
                    <a href="javascript:;">2023</a>
                </h2>

        <div class="chart" ref="chart"></div>
    </div>
</template>

<script>

export default{
    data(){
        return{

        };
    },
    methods:{
        createChart(){
            var myChart = this.$echarts.init(this.$refs.chart);
            // 年份数据
var yearData = [{
            year: "2022", // 年份
            data: [
                // 两个数组是因为有两条线
                [24, 40, 101, 134, 90, 230, 210, 230, 120, 230, 210, 120],
                [40, 64, 191, 324, 290, 330, 310, 213, 180, 200, 180, 79]
            ]
        },
        {
            year: "2023", // 年份
            data: [
                // 两个数组是因为有两条线
                [123, 175, 112, 197, 121, 67, 98, 21, 43, 64, 76, 38],
                [143, 131, 165, 123, 178, 21, 82, 64, 43, 60, 19, 34]
            ]
        }
    ];

    var option = {
        // 通过这个color修改两条线的颜色
        color: ["#00f2f1", "#ed3f35"],
        tooltip: {
            trigger: "axis"
        },
        legend: {
            // 如果series 对象有name 值，则 legend可以不用写data
            // 修改图例组件 文字颜色
            textStyle: {
                color: "#4c9bfd"
            },
            // 这个10% 必须加引号
            right: "10%"
        },
        grid: {
            top: "20%",
            left: "3%",
            right: "4%",
            bottom: "3%",
            show: true, // 显示边框
            borderColor: "#012f4a", // 边框颜色
            containLabel: true // 包含刻度文字在内
        },

        xAxis: {
            type: "category",
            boundaryGap: false,
            data: [
                "1月",
                "2月",
                "3月",
                "4月",
                "5月",
                "6月",
                "7月",
                "8月",
                "9月",
                "10月",
                "11月",
                "12月"
            ],
            axisTick: {
                show: false // 去除刻度线
            },
            axisLabel: {
                color: "#4c9bfd" // 文本颜色
            },
            axisLine: {
                show: false // 去除轴线
            }
        },
        yAxis: {
            type: "value",
            axisTick: {
                show: false // 去除刻度线
            },
            axisLabel: {
                color: "#4c9bfd" // 文本颜色
            },
            axisLine: {
                show: false // 去除轴线
            },
            splitLine: {
                lineStyle: {
                    color: "#012f4a" // 分割线颜色
                }
            }
        },
        series: [{
                name: "新增岗位",
                type: "line",
                // smooth:true 可以让我们的折线显示带有弧度
                smooth: true,
                data: yearData[0].data[0]
            },
            {
                name: "新增求职人",
                type: "line",
                smooth: true,
                data: yearData[0].data[1]
            }
        ]
    };

    // 3. 把配置给实例对象
    myChart.setOption(option);
    // 4. 让图表跟随屏幕自动的去适应
    window.addEventListener("resize", function () {
        myChart.resize();
    });

    // 5.点击切换效果
    // $(".line h2").on("click", "a", function () {
    //     // alert(1);
    //     // console.log($(this).index());
    //     // 点击 a 之后 根据当前a的索引号 找到对应的 yearData的相关对象
    //     // console.log(yearData[$(this).index()]);
    //     var obj = yearData[$(this).index()];
    //     option.series[0].data = obj.data[0];
    //     option.series[1].data = obj.data[1];
    //     // 需要重新渲染
    //     myChart.setOption(option);
    // });
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