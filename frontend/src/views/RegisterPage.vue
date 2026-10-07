<template>
  <div class="register">
    <div class="register_box">
      <div class="header">
        <div class="fl" style="font-size: 14px;" @click="backHome">返回首页</div>
        <div class="fr" style="font-size: 14px;" @click="goLogin">已有账户？去登录</div>
      </div>
      <div id="register_form">
        <h1 class="logo"><router-link :to="{ path: '/home', exact: true }">Jobpilot</router-link></h1>
        <div class="form-group" style="margin-bottom: 25px;">
          <input type="text" class="form-control" id="username" name="username" v-model="username" placeholder="请输入用户名" />
        </div>
        <div class="form-group" style="margin-bottom: 25px;">
          <input class="form-control" type="text" placeholder="请输入邮箱" v-model="email">
        </div>
        <div class="form-group" style="margin-bottom: 25px;">
          <input class="form-control" type="text" id=mes placeholder="请输入验证码" v-model="captcha">
          <button @click="getCaptcha">获取验证码</button>
        </div>
        <label>用户名：4-20个字符，支持汉字、字母、数字2种及以上组合</label>
        <div class="form-group" style="margin-bottom: 25px;">
          <input class="form-control" type="text" placeholder="请输入手机号" v-model="phone">
        </div>
        <div class="form-group">
          <input type="password" class="form-control" id="password" name="password" v-model="password"
            placeholder="请输入密码" />
        </div>
        <label for="">密码：8-16个非连续或重复的字符</label>
        <div class="form-group">
          <input type="password" class="form-control" id="passconfirm" name="passwordConfirm" v-model="passwordConfirm"
            placeholder="请确认密码" />
        </div>
        <div class="form-group" style="border: none;">
          <input type="checkbox" style="vertical-align: middle;">
          <em>我已阅读并同意<a href="#">《用户协议》</a><a href="#">《登录政策》</a><a href="#">《隐私条款》</a></em>
        </div>
        <button class="btn-success" @click="registerBtn">
          注册
        </button>
        <!-- <input type="submit" value="tijiao" /> -->
      </div>
    </div>
  </div>
</template>
<script>
import { verifyCaptcha } from "../api/user";
import { userRegister } from "../api/user";
import { getCaptcha as requestCaptcha } from "../api/user";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      passwordConfirm: "",
      phone: "",
      captcha: "",
    };
  },
  methods: {
    backHome() {
      this.$router.push("/home");
    },
    goLogin() {
      this.$router.push("/login");
    },
    getCaptcha() {
      if (!this.username || !this.email) return alert("请先填写用户名和邮箱");
      requestCaptcha({ username: this.username, email: this.email }).then((res) => {
        if (res.code === 200) alert("验证码已发送");
        else alert(res.msg || "验证码发送失败");
      }).catch((error) => {
        console.error("验证码请求出错:", error);
        alert("验证码发送失败，请稍后重试");
      });
    },
    registerBtn() {
      if (this.username == "") {
        alert("用户名不能为空");
        return;
      } else if (this.password == "") {
        alert("密码不能为空");
        return;
      } else if (this.email == "") {
        alert("邮箱不能为空");
        return;
      } else if (this.phone == "") {
        alert("手机号不能为空");
        return;
      } else if (this.captcha == "") {
        alert("验证码不能为空");
        return;
      } else if (this.password !== this.passwordConfirm) {
        alert("两次输入的密码不一致");
        return;
      }
      else {
        verifyCaptcha({
          captcha: this.captcha,
          email: this.email,
          username: this.username,
        }).then(res => {
          if (res["code"] === 200) {
            userRegister({
              username: this.username,
              email: this.email,
              password: this.password,
              phone: this.phone,
            }).then((registerResult) => {
              if (registerResult.code === 200) {
                alert("注册成功，请登录");
                this.$router.push("/login").catch((err) => err);
              } else {
                alert(registerResult.msg || "注册失败");
              }
            }).catch((error) => {
              console.error("注册出错:", error);
            })
          }
        })
          .catch((error) => {
            console.error("检查验证码出错:", error);
            alert("验证码错误");
          })
      }
    },
  },
  //   created() {},
};
</script>

<style lang="less" scoped>
@import '../less/reset.less';

.logo {
  height: 30px;
  width: 125px;
  margin-bottom: 30px;
  margin-top: 20px;
}

.logo a {
  display: block;
  width: 140px;
  height: 34px;
  background: url(../assets/logo.png) no-repeat;
  background-size: 100% 100%;
  font-size: 0;
  margin-left: 125px;
}

.register {
  width: 100%;
  height: 100%;
  background-color: #f7f7f8;
  overflow: auto;
}

.register_box {
  width: 435px;
  margin: 0 auto;
  color: #333;

  .header {
    height: 20px;
    margin: 0px auto 15px auto;
    padding-top: 7px;
    text-align: center;
  }

  #register_form {
    padding: 20px;
    margin-bottom: 15px;
    text-align: left;
    border: 1px solid #d8dee2;
    border-radius: 5px;
    background-color: #fff;
  }
}

.form-group {
  width: 365px;
  height: 45px;
  margin: 10px auto;
  line-height: 45px;
  text-align: left;
  border: 1px solid lightgray;
  border-radius: 3px;
}

label {
  padding-left: 20px;
  color: gray;
}

.form-group:nth-child(1) {
  margin-bottom: 25px;
}

.form-group input {
  padding-left: 20px;
  height: 42px;
  font-size: 14px;
}

.form-group button {
  width: 120px;
  height: 37px;
  margin-left: 35px;
  line-height: 37px;
  border-radius: 3px;
  background-color: #0a65cc;
  color: #fff;
}

a {
  color: #0a65cc;
}

.btn-success {
  width: 365px;
  height: 45px;
  font-size: 16px;
  background-color: #0a65cc;
  color: #fff;
  border-radius: 3px;
  margin-left: 15px;
}
</style>
