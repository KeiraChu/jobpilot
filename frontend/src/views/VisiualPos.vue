<template>
    <div class="visual">    
        <div class="tim">{{ currentTime }}</div>  
        <section class="mainbox">
            <div class="column">
                <div class="panel"> <pos-chart/><div class="panel-footer"></div> </div>
                <div class="panel"> <emp-chart/><div class="panel-footer"></div> </div>
                <div class="panel"> <age-chart/><div class="panel-footer"></div> </div>
            </div>
            <div class="column">
              <div class="map">
                <!-- 地球 -->
                <div class="map1"></div>
                <!-- 旋转的网格球体 -->
                <div class="map2"></div>
                <!-- 箭头旋转 -->
                <div class="map3"></div>
                <!-- 地图模块 -->
                <div class="chart"><map-chart/></div>
            </div>
            </div>
            <div class="column">
              <div class="panel"> <work-chart/><div class="panel-footer"></div> </div>
              <div class="panel"> <edu-chart/><div class="panel-footer"></div> </div>
              <div class="panel"> <loc-chart/><div class="panel-footer"></div> </div>
            </div>
        </section>
        <div class="key">
          <div class=""> <cloud-chart/>
            <!-- <div class="panel-footer"></div>  -->
          </div>
        </div>
    </div>
</template>
<script>
import WorkChart from '../components/WorkChart.vue'; 
import EduChart from '../components/EduChart.vue';
import PosChart from '../components/PosChart.vue';
import EmpChart from '../components/EmpChart.vue';
import AgeChart from '../components/AgeChart.vue';
import MapChart from '../components/MapChart.vue';
import LocChart from '../components/LocChart.vue';
import CloudChart from '../components/CloudChart.vue';
import * as echarts from 'echarts';  
import 'echarts-wordcloud';  
import $ from 'jquery'; 

export default {  
  data() {  
    return {  
      currentTime: null, 
    };  
  },  
  components: {  
    EmpChart,
    EduChart,
    PosChart,
    AgeChart,
    MapChart,
    EduChart,
    WorkChart,
    LocChart,
    CloudChart,
  },
  mounted() {  
    this.updateTime(); 
  },  
  methods: {  
    updateTime() {  
      setInterval(() => {  
        const dt = new Date();  
        this.currentTime = `当前时间：${dt.getFullYear()}年${dt.getMonth() + 1}月${dt.getDate()}日 - ${dt.getHours()}时${dt.getMinutes()}分${dt.getSeconds()}秒`;  
      }, 1000);  
    },  
  },  
};  

</script>
<style lang="less">
.visual{
    margin: 0;
    background: url(../assets/image/bg.jpg) no-repeat top center;
    width: 100%;
    height: 850px;
}
.tim {
    text-align: right;
    color: #fff;
}
.mainbox {
  min-width: 1024px;
  max-width: 1920px;
  margin: 0 auto;
  padding: 0.125rem 0.125rem 0;
  display: flex;
}
.mainbox .column {
  flex: 2.5;
}
.mainbox .column:nth-child(2) {
  flex: 5;
  margin: 0 0.125rem 0.1875rem;
  overflow: hidden;
}
.mainbox .panel {
  position: relative;
  height: 35%;
  border: 1px solid rgba(25, 186, 139, 0.17);
  background: url(../assets/image/line\(1\).png) rgba(255, 255, 255, 0.03);
  padding: 0 0.1875rem 0.5rem 0.7rem;
  margin-bottom: 0.1875rem;
}
.mainbox .panel::before {
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}
.mainbox .panel::after {
  position: absolute;
  top: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}
.mainbox .panel .panel-footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}
.mainbox .panel .panel-footer::before {
  position: absolute;
  bottom: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}
.mainbox .panel .panel-footer::after {
  position: absolute;
  bottom: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}
.mainbox .panel h2 {
  height: 20px;
    color: #fff;
    font-size: 12px;
    line-height: 27px;
  text-align: center;
  font-weight: 400;
}
.map {
  position: relative;
  height: 100%;
}
.map .map1 {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 400px;
  background: url(../assets/image/map.png);
  background-size: 100% 100%;
  opacity: 0.3;
}
.map .map2 {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 420px;
  height: 420px;
  background: url(../assets/image/lbx.png);
  background-size: 100% 100%;
  opacity: 0.6;
  animation: rotate1 15s linear infinite;
}
.map .map3 {
  position: absolute;
  top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 440px;
    height: 440px;
  background: url(../assets/image/jt.png);
  background-size: 100% 100%;
  opacity: 0.6;
  animation: rotate2 10s linear infinite;
}
.map .chart {
  position: absolute;
  top: 0%;
  left: 0;
  width: 100%;
  height: 500px;
}
.key{
  // height: 300px;
  margin-top: 5%;
}
// .key h2{
//     text-align: left;
//     color: #fff;
//     margin-left: 15%;
// }
</style>