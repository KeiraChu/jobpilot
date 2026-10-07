<template>
    <div class="clogin">
        <div class="header w">
            <!-- logo模块 -->
            <div class="logo">
                <h1>
                    <h1>
                <router-link to="/home">Jobpilot</router-link>
            </h1>
                </h1>
            </div>
                <a class="reg" @click="Register">注册</a>
                <div class="tel"><i class="el-icon-service"></i>联系客服</div>
                <div class="help">帮助中心</div>
        </div>
        <div class="area">
            <div class="cloginarea w">
                <div class="clog_fl">
                    <img src="../assets/image/clogin.png" alt="">
                </div>
                <!-- 表单区域 -->
                <div class="clog_fr">
                    <div class="log-form">
                        <div class="top">
                            <p>
                                <router-link to="/login">我要求职</router-link>
                            </p>
                        </div>
                        <div class="topic">
                            <div class="login-option" :class="{ underline: isCaptchaActive }" @click="isCaptchaActive = true; isPasswordActive = false">验证码登录  
                            </div>  
                            <div class="login-option" :class="{ underline: isPasswordActive }" @click="isCaptchaActive = false; isPasswordActive = true">密码登录  
                            </div>  
                        </div>
                        <div v-show="isCaptchaActive" id="codeLoginForm">
                            <form>
                                <ul>
                                    <li><input class="ef" type="text" placeholder="请输入邮箱" value=""></li>
                                    <li><input class="mes" type="text" placeholder="短信验证码" value=""><button>获取验证码</button>
                                    </li>
                                    <li><button type="button" class="p_but">登 录</button></li>
                                    <li>
                                        <input type="checkbox">
                                        <label for="isread">我已阅读并同意<a href="#">《用户协议》</a><a href="#">《登录政策》</a></label>
                                        <a href="#">《隐私条款》</a>
                                    </li>
                                </ul>
                            </form>
                        </div>
                        <!-- 密码登录表单 -->
                        <div  v-show="isPasswordActive">
                            <form>   
                                <ul>
                                    <li><input class="ef"  type="text" placeholder="手机号码/邮箱/用户名" value=""></li>
                                    <li><input class="ef"  type="password" placeholder="密码" value=""><a href="#">忘记密码？</a>
                                    </li>
                                    <li><button type="button" class="p_but" id="login_btn_withPwd">登 录</button></li>
                                    <li>
                                        <input type="checkbox">
                                        <label for="isread">我已阅读并同意<a href="#">《用户协议》</a><a href="#">《登录政策》</a></label>
                                        <a href="#">《隐私条款》</a>
                                    </li>
                                </ul>
                            </form> 
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>  
export default {  
  data() {  
    return {  
      isCaptchaActive: true, 
      isPasswordActive: false  
    };  
  },
  methods: {
    Register(){
        this.$router.push("/register");
    }
  }
} 
</script> 
<style lang="less" scoped>
@import '../less/reset.less';
/* 头部 */
.header{
    height: 80px;
}
.logo {
    position: relative;
    top: 20px;
    height: 30px;
    width: 125px;
}

.logo a {
    display: block;
    width: 125px;
    height: 30px;
    background: url(../assets/logo.png) no-repeat;
    background-size: 100% 100%;
    font-size: 0;
}
/* 头部 */
.header .help,.tel,.reg{
    position: absolute;
    top: 25px;
    font-size: 14px;
    font-weight: 600;
    color: black;
}
.header .help{
    right: 140px;
}

.header .tel {
    right: 220px;
}

.header .reg {
    right: 320px;
    
    color: #0a65cc;
}

/* 内容部分 */
.area {
    width: 100%;
    height: 568px;
    background-color: #F7F7F8;
}

.cloginarea img {
    height: 307px;
    margin: 85px 40px 0 0;
}

.clog_fl {
    float: left;
    width: 39%;
}

.clog_fr {
    float: left;
    width: 500px;
    text-align: left;
    margin-top: 70px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, .1);
    border-radius: 15px;
}

.clog_fr .log_form {
    width: 400px;
    height: 500px;
    border-radius: 5px;
    margin-top: 20px;
}
.top p {
    margin: 10px auto auto 20px;
    font-size: 14px;
}
.top a:hover {
    color: #0a65cc;
}
/* 登录方式 */
.log-form .topic {
    display: flex;
    /* 使用 flex 布局 */
    justify-content: center;
    /* 在主轴上居中对齐 */
    gap: 20px;
    /* 设置元素之间的间距 */
    height: 60px;
    line-height: 60px;
    font-size: 20px;
}
.login-option {  
  cursor: pointer;
  text-decoration: none;
}  
  
.underline {  
border-bottom: 3px solid #0a65cc;
}
/* 验证表单 */
#accountLoginForm {
    display: none;
    /* 初始状态下隐藏账户登录表单 */
}
#codeLogin,
#accountLogin {
    text-align: center;
    width: 120px;
}

.topic div:hover {
    color: #0a65cc;
}

.log-form ul li {
    height: 55px;
    width: 350px;
    margin-left: 75px;
    margin-top: 15px;
}

.log-form ul li input {
    width: 350px;
    line-height: 40px;
    background-color: #F8F9FA;
    border-radius: 3px;
}

.log-form ul li a {
    color: black;
    float: right;
}

#codeLoginForm li:nth-child(2) input {
    width: 180px;
    margin-right: 20px;
}

#codeLoginForm li:nth-child(2) button {
    width: 150px;
    height: 40px;
    background-color: #D3E3FD;
    color: #0a65cc;
    font-weight: 600;
    border-radius: 3px;
}

/* 登录按钮 */
.p_but {
    width: 350px;
    height: 40px;
    font-size: 17px;
    font-weight: 500;
    background-color: #0a65cc;
    color: #fff;
    border-radius: 5px;
}

.log-form ul li:nth-child(4) input {
    width: 10px;
    height: 10px;
}

.log-form ul li:nth-child(4) a {
    color: #0a65cc;
    margin-left: -10px;
}
</style>