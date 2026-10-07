<template>
    <div class="login">
        <div class="header w">
        <!-- logo模块 -->
        <div class="logo">
            <h1>
                <router-link :to="{ path: '/home', exact: true }">Jobpilot</router-link>
            </h1>
        </div>
        <a class="reg" @click="Register">注册</a>
        <div class="tel"><i class="el-icon-service"></i>联系客服</div>
        <div class="help">帮助中心</div>
        </div>
    
        <div class="loginarea w">
        <!-- 系统特点 -->
        <div class="log_fl">
            <div class="fl_c">
                <i class="el-icon-s-custom"></i>
                <div class="fl_cn">
                    <p>多样化</p>
                    <div class="c_999">人才资源、岗位信息</div>
                </div>
            </div>
            <div class="fl_c">
                <i class="el-icon-s-promotion"></i>
                <div class="fl_cn">
                    <p>方便快捷</p>
                    <div class="c_999">在线招聘、省时省力</div>
                </div>
            </div>
            <div class="fl_c">
                <i class="el-icon-share"></i>
                <div class="fl_cn">
                    <p>准确匹配</p>
                    <div class="c_999">能力要求、快速推荐</div>
                </div>
            </div>

        </div>
        <div class="log_fr">
            <div class="top">
                <p>
                    <router-link :to="{ path: '/clogin', exact: true }">我要招聘</router-link>
                </p>
            </div>

            <div class="log-form">
                        <div class="topic">
                            <div class="login-option underline">密码登录
                            </div>
                        </div>
                        <!-- 密码登录表单 -->
                        <div  v-show="isPasswordActive">
                            <form>   
                                <ul>
                                    <li><input class="ef"  type="text" placeholder="手机号码/邮箱/用户名" v-model="acount"></li>
                                    <li><input class="ef"  type="password" placeholder="密码" v-model="password"><a href="#">忘记密码？</a>
                                    </li>
                                    <li><button type="button" class="p_but" id="login_btn_withPwd" @click="loginPwd">登 录</button></li>
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
</template>

<script>

// import { Password } from 'ant-design-vue/types/input/password';
import { userLogin } from "../api/user";
export default {
  data() {  
    return {  
      isPasswordActive: true,
      acount:"",
      password:"",
    };  
  },
  methods: {
    Register(){
        this.$router.push("/register");
    },
    loginPwd(){
        if (this.acount == "") {
            alert("账号不能为空");
            return;
        } else if (this.password == "") {
            alert("密码不能为空");
            return;
        }else{
        userLogin({
            account: this.acount,
            password: this.password,
        }).then(res => {
            if (res.code == 200) {
              localStorage.setItem('token', res.data.token);
              localStorage.setItem('userId', res.data.user_id);
              this.$router.push("/home").catch((err) => err);
              alert("登录成功");
              this.$store.commit('setFlagToTrue');
            } else {
              alert(res.msg);
            }
        }).catch((error) => { 
            console.error("登录请求出错:", error);
        });
        }
    }
  }
};  
</script>
<style lang="less" scoped>
@import '../less/reset.less';
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

/* 登录内容区 */
.loginarea {
    margin-top: 90px;
}

.log_fl {
    float: left;
    width: 28%;
    height: 360px;
    margin-left: 11%;
    border-radius: 15px 0 0 15px;
    background: linear-gradient(to bottom left, #ECF7FC, #fff);
    box-shadow: -4px 0 12px rgba(0, 0, 0, .1);
}

.fl_c {
    display: flex;
    align-items: center;
    text-align: left;
    height: 100px;
}

.fl_c i {
    margin: 0 20px;
    font-size: 35px;
    color: #0a65cc;
}

.fl_cn p {
    font-size: 15px;
    color: #666;
}

.c_999 {
    font-size: 13px;
    color: #999;
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

.log_fr {
    float: left;
    width: 500px;
    height: 360px;
    border-radius: 0 15px 15px 0;
    box-shadow: 4px 0 12px rgba(0, 0, 0, .1);
}

.log_fr .top p {
    text-align: left;
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
.log-form .check{
    text-align: left;
}
</style>
