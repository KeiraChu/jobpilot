<template>
    <div class="assess w">
        <div class="info">
            <div class="title">
                <h2>能力评价</h2>
                <p>通过您的简历与现有职位要求匹配后，现对您求职职位的要求反馈如下：</p>
            </div>
            <div class="chart">
                <div class="all" style="position: relative;text-align: left;display: inline-block;width: 95%;margin-top: 2%;margin-left: 6%;">
                <i class="el-icon-user-solid" style="display: inline-block;font-size: 40px;float: left;margin-right: 2%;"></i>
                <p>赖小玥的整体匹配度为70.6分</p>
                <p>高于全国72%的人。推荐指数：<el-rate v-model="value" disabled   score-template="{value}" style="display: inline-block; margin: 10px 0">
          </el-rate></p>
          <p style="position: absolute;font-size: 30px;font-weight: 600;color:#F7BA2A;top: 10px;right: 90px;">70.6%</p>
                </div>
                <br>
                <div style="text-align: left;margin:1% 5%;">
                    <p>您的简历与推荐职位的匹配度为70.6%;您的项目经历、期望城市、工作经历、专业技能与推荐职位要求都有较高匹配度，但是您的期望薪资、教育经历与推荐职位的匹配度中等，您可以考虑调节您的期望薪资或者查看更多不限学历的职位。</p>
                </div>
                <div class="panel1"><per-chart/></div><br>
                <div class="panel2"><know-chart/></div><br>
                <div class="panel3"><radar-chart/></div><br>
                <div class="panel4" style="position: relative;height: 350px;">
                    <h2>mbti职业性格分析</h2>
                    <a-input class="mt-2" placeholder="请输入您的mbti查看适合您的就业指导" v-model="mbti" style="float: left;width: 300px;"/>
                    <div class="cc" style="width: 230px;margin-top: 7%;">
                        <img src="../assets/image/enfp.png" alt="">
                        <div style="position: absolute;left:20%;top:60px;"><mbti-rader/></div>
                        <div style="width: 430px;margin-top: 50px;border: 2px solid rgb(94, 229, 224);border-radius: 5px;padding: 10px;position: absolute;bottom: 0;right: 0;">
                            <el-collapse v-model="activeNames" @change="handleChange">
                                <el-collapse-item name="1">
                                    <template slot="title">
                                        <p style="color: #F7BA2A;font-weight: 600;">enfp工作上的优势<i class="el-icon-s-opportunity"></i></p>
                                    </template>
                                    <div class="content">拥有承担风险、尝试新东西和克服阻碍的勇气；</div>
                                    <div class="content">优秀的沟通技巧和能力，激发起别人的激情；</div>
                                    <div class="content">容易接受他人，理解他人的需求和动机。</div>
                                </el-collapse-item>
                                <el-collapse-item name="2">
                                    <template slot="title">
                                        <p style="color: rgb(94, 229, 224);font-weight: 600;">工作上的劣势<i class="el-icon-s-marketing"></i></p>
                                    </template>
                                    <div class="content">在处理和遵循重要细节时缺乏纪律；</div>
                                    <div class="content">难以设置优先次序和做决定；</div>
                                    <div class="content">有无条理、无组织、无安排的倾向（tendency to be disorganized）</div>
                                </el-collapse-item>
                                <el-collapse-item name="3">
                                    <template slot="title">
                                        <p style="color: rgb(104, 202, 237);;font-weight: 600;">人群中受欢迎的职业<i class="el-icon-s-shop"></i></p>
                                    </template>
                                    <div class="content">创造性：电影编剧、戏剧作家、教育软件开发人员；</div>
                                    <div class="content">技术：项目经理、员工倡导（技术顾问）；</div>
                                    <div class="content">还有市场营销/策划、教育/咨询、企业/商业等方面的更多工作</div>
                                </el-collapse-item>
                                </el-collapse>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import KnowChart from '../components/KnowChart.vue';
import PerChart from '@/components/PerChart.vue';
import RadarChart from '@/components/RadarChart.vue';
import MbtiRader from '../components/MbtiRader.vue';
export default {  
  data() {  
    return {
        value: 3.5,
        mbti:'enfp',
        activeNames: ['1']
    };  
  },  
  methods: {
      handleChange(val) {
      }
    },
  components: {
    KnowChart,
    PerChart,
    RadarChart,
    MbtiRader,
    }
}
</script>

<style lang="less" scoped>
.w{
    // width: 80%;
    margin: 10px auto;
}
.assess .chart{
    background: linear-gradient(to bottom, #E6F3FB, #fff); 
    height: 100%;
}
.info {
    display: inline-block;
    width: 68%;
}
.assess .info .title{
    text-align: left;
}
.assess .info .title h2{
    font-size: 20px;
    font-weight: 600;
}
.panel1{
    display: inline-block;
    margin-bottom: 10px;
}
.panel2{
    display: inline-block;
    margin-bottom: 10px;
}
.panel3{
    margin-left: 10%;
}
h2{
    font-size: 20px;
    font-weight: 600;
    text-align: left;
}
.content{
    text-align: left;
    font-weight: 600;
}
</style>