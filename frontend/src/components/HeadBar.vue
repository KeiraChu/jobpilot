<!-- eslint-disable-next-line vue/multi-word-component-names -->  
<template>   
    <div class="header">
            <!-- 快捷导航模块 -->
    <section class="shortcut">
        <div class="logo">
                    <h1>
                        <router-link :to="{ path: '/home', exact: true }">Jobpilot</router-link>
                    </h1>
                </div>
        <div class="w">
            <div class="fl">
                <el-menu
                    :default-active="$store.state.activeIndex"
                    class="el-menu-demo"
                    mode="horizontal"
                    @select="handleSelect"
                    background-color="#f1f2f4"
                    text-color="black"
                    active-text-color="#0a65cc"
                    >
                    <el-menu-item index="1" @click="goHome">首页</el-menu-item>
                    <el-menu-item index="2" @click="goResume">简历</el-menu-item>
                    <el-menu-item index="3" @click="goPosition">推荐职位</el-menu-item>
                    <el-menu-item index="6" @click="goCopilot">AI求职助手</el-menu-item>
                    <el-menu-item index="4" @click="goAssess">评估</el-menu-item>
                    <el-menu-item index="5" @click="goVisual">统计数据</el-menu-item>
                </el-menu>
            </div>
            <div class="fr">
                    <el-cascader
                        class="select"
                        size="medium "
                        :options="options"
                        placeholder="请选择期望城市"
                        v-model="selectedOptions"
                        @change="handleChange"
                    >
                    </el-cascader>
                    <!-- <div class="info"  v-if="flag"> -->
                        <div class="info" >
                        <i class="el-icon-chat-line-round"></i>
                        <em class="spot"></em>
                        <!-- <img src="../assets/image/favicon.png" alt=""> -->
                        <el-dropdown @command="handleCommand">
                            <span class="el-dropdown-link">
                                <img src="../assets/image/favicon.png" alt="">
                            </span>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item command="person">个人中心</el-dropdown-item>
                                <el-dropdown-item >消息中心</el-dropdown-item>
                                <el-dropdown-item >退出登录</el-dropdown-item>
                            </el-dropdown-menu>
                            </el-dropdown>
                    </div>
                    <!-- <div class="btn" v-else>
                        <button class="employee" @click="navigateToLogin">
                        登录
                    </button> 
                    </div>-->
            </div>
        </div>
    </section>
    </div>
</template>
<script> 
import { regionData} from "element-china-area-data";
export default {
    data() {
    return {
        options: regionData,
        selectedOptions: [],
      };
    // return {
    //   locationOptions: [], // 位置的选项数据，根据实际情况初始化
    //   options: provinceAndCityData,
    //   selectedOptions: [],
    //   selectedLocation: [] // 添加选中的位置数据
    // };
  },
//   mounted() {
//     this.getLocation(); // 页面加载时获取用户位置
//   },
created() {  
  },  
  methods: {
    handleSelect(index) {  
      this.$store.dispatch('setActiveMenuItem', index); // 调用 action 更新 state  
      // 将 activeIndex 保存到本地存储  
      localStorage.setItem('activeIndex', index);  
    },
    handleChange(value) {
    },
    handleCommand(command){
        switch (command) {  
        case 'person':  
          this.$router.push('/person'); 
          break;  
          default:  
          break;
        }
    },
    goHome(){
        this.$router.push("/home").catch((err) => err);
    },
    goPosition(){
        this.$router.push("/position").catch((err) => err);
    },
    goResume(){
        this.$router.push("/about").catch((err) => err);
    },
    goAssess(){
        this.$router.push("/assess").catch((err) => err);
    },
    goCopilot(){
        this.$router.push("/career-copilot").catch((err) => err);
    },
    goVisual(){
        this.$router.push("/visual").catch((err) => err);
    },
    // goPerson(){
    //     this.$router.push("/about").catch((err) => err);
    //     console.log("个人中心");
    // },
    // async getLocation() {
    //   try {
    //     const response = await axios.get('https://restapi.amap.com/v3/ip?key=a4c963b35454f8fdd2e114db87befbf4'); // 发起请求获取用户地理位置
    //     const location = response.data; // 获取地理位置信息
    //     this.selectedLocation = [location.province, location.city]; // 设置用户位置
    //   } catch (error) {
    //     console.log('获取地理位置失败：', error);
    //   }
    // },
    // handleLocationChange(value) {
    //   console.log('选择的位置：', value);
    //   // 处理位置变化的逻辑
    // },
    navigateToLogin() {  
        this.$router.push("/login").catch((err) => err);
    },
  },
}    
</script>
<style lang=less scoped>
@import '../less/reset.less';
/* 快捷导航模块 */
.shortcut {
    height: 45px;
    line-height: 35px;
    background-color: #f1f2f4;
}
.shortcut ul li {
    float: left;
}
.el-menu--horizontal>.el-menu-item {
    float: left;
    height: 44px;
    line-height: 44px;
    font-size: 16px;
}
.shortcut .fr{
    position: relative;
    height: 35px;
    line-height: 35px;
}

.shortcut .fr span {
    color: black;
}
.select {
margin-top: 1%;
margin-right:100px ;
}

.logo {
    position: absolute;
    top: 1%;
    left: 6%;
    border-radius: 5px;
    overflow: hidden;
    height: 30px;
    width: 135px;
}

.logo a {
    display: block;
    width: 122px;
    height: 30px;
    background: url(../assets/logo.png) no-repeat;
    background-size: 100% 100%;
    font-size: 0;
}

/* 登录按钮 */
.btn{
    position: absolute;
    float: right;
    right: 0px;
    top: 4px;
}
.btn .employee {
    width: 70px;
    height: 35px;
    background-color: #fff;
    color: #0a65cc;
    border: 1px solid #dbe8f7;
    border-radius: 3px;
    font-weight: 600;
}
.info {
    position: absolute;
    float: right;
    right: 0px;
    top: 2px;
}
i.el-icon-chat-line-round {
    position: absolute;
    float: right;
    font-size: 20px;
    top: 7px;
    right: 58px;
}
.info img {
    width: 40px;
    height: 40px;
    border-radius: 15px;
    margin-left: 15px;
}

.info .spot {
    position: absolute;
    float: right;
    top: 4px;
    right: 57px;
    width: 12px;
    height: 12px;
    background-color: red;
    border-radius: 10px;
    border: 2px solid #fff;
}
::before {
    font-weight: 600;
}
</style>
