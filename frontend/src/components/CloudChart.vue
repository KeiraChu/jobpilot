<template>
    <div class="wordcloud">
        <!-- <h2>热门关键</h2> -->
      <div class="chart" ref="chart"></div>
    </div>
</template>

<script>
import 'echarts-wordcloud'
export default{
    data(){
        return{
        }
    },
    methods:{
        createChart(){
            var ec_main = this.$echarts.init(this.$refs.chart);
            var ec_main_option = {
    tooltip: {
        show: false
    },
    series: [{
        type: 'wordCloud',
        gridSize: 1,
        sizeRange: [12, 55],
        rotationRange: [-45, 0, 45, 90],
        textStyle: {
  color: function() {
    return `rgb(${[
      Math.round(Math.random() * 200 + 55),
      Math.round(Math.random() * 200 + 55),
      Math.round(Math.random() * 200 + 55)
    ].join(',')})`
}
        },
        right: null,
        bottom: null,
        data: [{'name': '数据', 'value': 2252}, {'name': '大数', 'value': 2053}, {'name': '工程师', 'value': 1321}, {'name': '开发', 'value': 985}, {'name': '分析', 'value': 255}, {'name': '数据分析', 'value': 230}, {'name': '经理', 'value': 196}, {'name': '分析师', 'value': 154}, {'name': '高级', 'value': 136}, {'name': '架构', 'value': 131}, {'name': '方向', 'value': 128}, {'name': '平台', 'value': 127}, {'name': '架构师', 'value': 125}, {'name': '研发', 'value': 120}, {'name': '产品', 'value': 111}, {'name': '销售', 'value': 73}, {'name': '测试', 'value': 62}, {'name': '数据测试', 'value': 50}, {'name': '技术', 'value': 46}, {'name': '项目', 'value': 45}, {'name': '专家', 'value': 45}, {'name': '资深', 'value': 45}, {'name': '助理', 'value': 42}, {'name': '客户', 'value': 40}, {'name': '大客', 'value': 38}, {'name': '高级工', 'value': 36}, {'name': '运营', 'value': 32}, {'name': '接受', 'value': 32}, {'name': '双休', 'value': 31}, {'name': '应届', 'value': 31}, {'name': '软件', 'value': 30}, {'name': '实习', 'value': 29}, {'name': '试工', 'value': 29}, {'name': '中级', 'value': 27}, {'name': '算法', 'value': 27}, {'name': '中心', 'value': 26}, {'name': '实习生', 'value': 25}, {'name': '项目经理', 'value': 25}, {'name': '总监', 'value': 25}, {'name': '系统', 'value': 21}, {'name': '解决', 'value': 21}, {'name': '解决方案', 'value': 21}, {'name': '方案', 'value': 21}, {'name': '顾问', 'value': 21}, {'name': '数据项', 'value': 20}, {'name': '信息', 'value': 19}, {'name': '北京', 'value': 19}, {'name': '业大', 'value': 18}, {'name': '教师', 'value': 18}, {'name': '城市', 'value': 18}, {'name': '师资', 'value': 17}, {'name': '讲师', 'value': 16}, {'name': '研究', 'value': 16}, {'name': '管理', 'value': 16}, {'name': '智慧', 'value': 15}, {'name': '负责', 'value': 15}, {'name': '负责人', 'value': 15}, {'name': '责人', 'value': 15}, {'name': '电商', 'value': 15}, {'name': '台架', 'value': 15}, {'name': '专员', 'value': 14}, {'name': '政务', 'value': 14}, {'name': '咨询', 'value': 14}, {'name': '数据安全', 'value': 14}, {'name': '台大', 'value': 14}, {'name': '据实', 'value': 13}, {'name': '实施', 'value': 13}, {'name': '服务', 'value': 13}, {'name': '数据中心', 'value': 13}, {'name': '流量', 'value': 13}, {'name': '理工', 'value': 12}, {'name': '据云', 'value': 12}, {'name': '计算', 'value': 12}, {'name': '人大', 'value': 12}, {'name': '经验', 'value': 11}, {'name': '治理', 'value': 11}, {'name': '软件开发', 'value': 11}, {'name': '数据挖掘', 'value': 11}, {'name': '挖掘', 'value': 11}, {'name': '后端', 'value': 11}, {'name': '前端', 'value': 11}, {'name': '医药', 'value': 10}, {'name': '数据仓库', 'value': 10}, {'name': '仓库', 'value': 10}, {'name': '售前', 'value': 10}, {'name': '需求', 'value': 10}, {'name': '智能', 'value': 10}, {'name': '实时', 'value': 10}, {'name': '中台', 'value': 10}, {'name': '试开', 'value': 10}, {'name': '联网', 'value': 9}, {'name': '客户经理', 'value': 9}, {'name': '业务', 'value': 9}, {'name': '研究员', 'value': 9}, {'name': '营销', 'value': 9}, {'name': '数据系统', 'value': 9}, {'name': '金融', 'value': 9}, {'name': '企业', 'value': 9}, {'name': '银行', 'value': 9}, {'name': '建模', 'value': 8}, {'name': '区域', 'value': 8}, {'name': '施工', 'value': 8}, {'name': '交付', 'value': 8}, {'name': '引擎', 'value': 8}, {'name': '广告', 'value': 8}, {'name': '数据处理', 'value': 7}, {'name': '行业', 'value': 7}, {'name': '人员', 'value': 7}, {'name': '设计', 'value': 7}, {'name': '软件工程', 'value': 7}, {'name': '开源', 'value': 7}, {'name': '可视', 'value': 7}, {'name': '可视化', 'value': 7}, {'name': '成都', 'value': 7}, {'name': '政府', 'value': 6}, {'name': '财务', 'value': 6}, {'name': '互联', 'value': 6}, {'name': '互联网', 'value': 6}, {'name': '信息化', 'value': 6}, {'name': '科学', 'value': 6}, {'name': '加班', 'value': 6}, {'name': '设计师', 'value': 6}, {'name': '前端开发', 'value': 6}, {'name': '主管', 'value': 6}, {'name': '级数', 'value': 6}, {'name': '产业', 'value': 5}, {'name': '老师', 'value': 5}, {'name': '数据管理', 'value': 5}, {'name': '商务', 'value': 5}, {'name': '深圳', 'value': 5}, {'name': '上海', 'value': 5}, {'name': '数据库', 'value': 5}, {'name': '据库', 'value': 5}, {'name': '市运', 'value': 5}, {'name': '博士', 'value': 5}, {'name': '录入', 'value': 5}, {'name': '备份', 'value': 5}, {'name': '时数', 'value': 5}, {'name': '直播', 'value': 5}, {'name': '团队', 'value': 5}, {'name': '离线', 'value': 5}, {'name': '武汉', 'value': 5}, {'name': '短视', 'value': 5}, {'name': '包住', 'value': 4}, {'name': '合肥', 'value': 4}, {'name': '运营商', 'value': 4}, {'name': '营商', 'value': 4}, {'name': '遥感', 'value': 4}, {'name': '地铁', 'value': 4}, {'name': '商业', 'value': 4}, {'name': '人工', 'value': 4}, {'name': '人工智能', 'value': 4}, {'name': '会计', 'value': 4}, {'name': '安全工程', 'value': 4}, {'name': '亚马', 'value': 4}, {'name': '亚马逊', 'value': 4}, {'name': '提供', 'value': 4}, {'name': '供住', 'value': 4}, {'name': '住宿', 'value': 4}, {'name': '主任', 'value': 4}, {'name': '不加', 'value': 4}, {'name': '底薪', 'value': 4}, {'name': '火山', 'value': 4}, {'name': '存储', 'value': 4}, {'name': '商大', 'value': 4}, {'name': '研究院', 'value': 4}, {'name': '模型', 'value': 4}, {'name': '脱敏', 'value': 4}, {'name': '师实', 'value': 4}, {'name': '电信', 'value': 4}, {'name': '科技', 'value': 4}, {'name': '技术部', 'value': 4}, {'name': '国际', 'value': 4}, {'name': '集成', 'value': 4}, {'name': '岗位', 'value': 4}, {'name': '代表', 'value': 3}, {'name': '数据业务', 'value': 3}, {'name': '自动', 'value': 3}, {'name': '驾驶', 'value': 3}, {'name': '质量', 'value': 3}, {'name': '工业', 'value': 3}, {'name': '中高', 'value': 3}, {'name': '中高级', 'value': 3}, {'name': '招商', 'value': 3}, {'name': '市场', 'value': 3}, {'name': '初级', 'value': 3}, {'name': '与会', 'value': 3}, {'name': '会计专业', 'value': 3}, {'name': '驻场', 'value': 3}, {'name': '工大', 'value': 3}, {'name': '录入员', 'value': 3}, {'name': '年底', 'value': 3}, {'name': '班底', 'value': 3}, {'name': '网络', 'value': 3}, {'name': '评估', 'value': 3}, {'name': '员工', 'value': 3}, {'name': '报销', 'value': 3}, {'name': '增长', 'value': 3}, {'name': '营工', 'value': 3}, {'name': '国内', 'value': 3}]
    }]
            }
            ec_main.setOption(ec_main_option);
            window.addEventListener("resize", function () {
                ec_main.resize();
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
// .wordcloud h2{
//     text-align: left;
// }
.chart{
    width: 100%;
    height: 200px;
}
</style>