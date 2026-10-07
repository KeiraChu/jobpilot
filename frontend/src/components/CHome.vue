<template>
    <div>
        <div class="one-info">
            <div class="w">
                <div class="fl">
                    <h1><p>为您提供</p><p>更符合公司职位要求的</p><p>工作岗位</p></h1>
                    <div class="resume">
                        <div class="trigger">  
                            <span>发布职位</span> 
                            <div class="upload">  
                                <span class="drop" @click="goResume"><i class="el-icon-edit"></i><p>在线编辑</p></span>  
                                <span class="drop" id="dropSpan" @click="showModal = true"><i class="el-icon-folder-add"></i><p>附件上传</p></span>
                                <!-- 弹框 -->  
                                <div v-if="showModal" class="modal">  
                                <div class="modal-content">  
                                    <div>
                                    <i class="el-icon-close" @click="showModal=false"></i>
                                    <p>支持DOC、DOCX、PDF、JPG、PNG格式附件</p>
                                    <p>文件大小不超过20M</p>
                                    <input type="file" ref="fileInput" @change="uploadFile" />  
                                    <button @click="upload">上传</button>
                                    </div>  
                                </div>  
                                </div>   
                            </div>
                        </div>
                    </div>
                </div>
                <div class="fr">
                        <img src="../assets/image/cbgi.jpg" alt="">
                </div>
                <div class="service">
                    <ul>
                        <li>
                            <i class="el-icon-suitcase-1"></i>
                            <div class="service_txt">
                                <h5>1,75,324</h5>
                                <p>求职者</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-office-building"></i>
                            <div class="service_txt">
                                <h5>97,354</h5>
                                <p>应届生</p>
                            </div>
                        </li>
                        <!-- <li>
                            <i class="el-icon-user"></i>
                            <div class="service_txt">
                                <h5>38,47,154</h5>
                                <p>求职者</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-suitcase-1"></i>
                            <div class="service_txt">
                                <h5>7,532</h5>
                                <p>新工作</p>
                            </div>
                        </li> -->
                    </ul>
                </div>
            </div>
        </div>
        <div class="two-info">
            <div class="w">
                <h3>Jobpilot将如何为您提供帮助</h3>
                <div class="help">
                    <ul>
                        <li>
                            <i class="el-icon-s-custom"></i>
                            <div class="help_txt">
                                <h5>创建账户</h5>
                                <p>更快捷地获得更多信息</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-upload"></i>
                            <div class="help_txt">
                                <h5>上传职位/简历</h5>
                                <p>更精准推荐适合你的简历/职位</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-zoom-in"></i>
                            <div class="help_txt">
                                <h5>找到合适的人选</h5>
                                <p>在网站帮助下更快找到人选</p>
                            </div>
                        </li>
                        <!-- <li>
                            <i class="el-icon-finished"></i>
                            <div class="help_txt">
                                <h5>申请工作</h5>
                                <p>支持在线与公司HR交流求职事宜</p>
                            </div>
                        </li> -->
                    </ul>
                </div>
            </div>
        </div>
        <!-- <div class="three-info">
            <div class="w">
                <div class="hot">
                    <h3>热门岗位</h3>
                    <button>查看更多 -></button>
                </div>
                <div class="position">
                    <ul>
                        <li>
                            <i class="el-icon-edit-outline"></i>
                            <div class="position_txt">
                                <h5>网文写手</h5>
                                <p>进行短篇小说创作</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-cpu"></i>
                            <div class="position_txt">
                                <h5>开发工程师</h5>
                                <p>小程序/网页开发</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-data-analysis"></i>
                            <div class="position_txt">
                                <h5>教师</h5>
                                <p>少儿特色教育</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-monitor"></i>
                            <div class="position_txt">
                                <h5>客服/运营</h5>
                                <p>网络客服/视频运营</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-headset"></i>
                            <div class="position_txt">
                                <h5>直播</h5>
                                <p>游戏主播</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-s-data"></i>
                            <div class="position_txt">
                                <h5>财务</h5>
                                <p>审计/会计</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-first-aid-kit"></i>
                            <div class="position_txt">
                                <h5>医疗健康</h5>
                                <p>药店店员/护士</p>
                            </div>
                        </li>
                        <li>
                            <i class="el-icon-coin"></i>
                            <div class="position_txt">
                                <h5>电气/通信</h5>
                                <p>电子工程师</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="four-info w">
            <div class="hot">
                    <h3>最热门的公司</h3>
            </div>
            <div class="company">
                <ul>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                    <li>
                        <i class="el-icon-basketball"></i>
                        <div class="service_txt">
                            <h5>承德昆孚商贸<span>最近热门</span></h5>
                            <p><i class="iconfont icon-dingwei"></i>承德·双滦区·元宝山大街</p>
                        </div>
                        <button>查看职位(3)</button>
                    </li>
                </ul>
            </div>
        </div> -->
        <!-- <div class="five-info">
            <eg-page></eg-page>
        </div> -->
        <div class="six-info w">
            <div class="register">
                <div class="fl">
                    <h2>成为求职者</h2>
                    <button @click="Register">现在就注册  -></button>
                </div>
                <div class="fr">
                    <h2>成为雇主</h2>
                    <button @click="Register">现在就注册  -></button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>  
import axios from "axios";
import EgPage from "../components/EgPage.vue";  
export default {  
  data() {  
    return {  
      showModal: false, // 控制弹框显示和隐藏的数据属性  
      file: null, // 选中的文件  
    };  
  }, 
  components: {
    EgPage,
  }, 
  methods: {
    Register(){
        this.$router.push("/register").catch((err) => err);
    },
    goResume(){
        this.$router.push("/about").catch((err) => err);
    },
    uploadFile() {  
      const file = this.$refs.fileInput.files[0];  
      this.file = file;  
    },  
    upload() {  
      if (!this.file) {  
        alert("请选择一个文件");  
        return;  
      }  
      const formData = new FormData();  
      formData.append("file", this.file);  
    
      // 在此处添加上传文件的逻辑  
      axios.post("https://example.com/upload", formData, {  
        headers: {  
          "Content-Type": "multipart/form-data",  
        },  
      })  
      .then(() => {  
        alert("上传成功");  
        this.showModal = false; // 上传成功后关闭弹框  
      })  
      .catch(() => {  
        alert("上传失败");  
      });  
    },  
  },  
};   
</script> 
<style lang=less scoped>
@import '../less/reset.less';
.one-info{
    height: 575px;
    background-color: #F7F7F8;
}
.one-info .fr{
    margin-bottom: 60px;
    width: 43%;
}
h1{
    color: black;
    font-size: 40px;
    font-weight: 600;
    margin-top: 60px;
    text-align: left;
}
.trigger{
    width: 100px;
    height: 45px;
    margin-top: 30px;
    margin-left: 50px;
    background: #fff;
    line-height: 45px;
    text-align: center;
    position: relative;
    overflow: hidden;
    border: 2px solid #0a65cc;
    border-radius: 5px;
    color: #0a65cc;
    font-size: 14px;
    font-weight: 600;
    position: relative;
}
.trigger:hover{
    overflow: visible;
    z-index: 999;
    cursor: pointer;
}
.upload{
    width: 150px;
    position: absolute;
    left: -28px;
}
.drop{
    display: inline-block;
    width: 75px;
    height: 80px;
    background: linear-gradient(to bottom, #ECF7FC, white);
    text-align: center;
    line-height: 40px;
    overflow: hidden;
}
.drop:hover{
    cursor: pointer;
}
.drop i{
    color: #0a65cc;
    font-size: 20px;
    font-weight: 600;
}
/* 弹框样式 */  
.modal {  
  display: block;  
  position: fixed;  
  z-index: 1;  
  padding-top: 100px;
  left: 0;  
  top: 0;  
  width: 100%;  
  height: 100%;  
  overflow: auto;  
  background-color: rgb(0,0,0);  
  background-color: rgba(0,0,0,0.4);  
}  
.modal-content {  
  background-color: #fefefe;  
  margin: auto;  
  padding: 20px;  
  border: 1px solid #888;  
  width: 40%;
  height: 35%;
  margin-top: 100px;  
}
input[type="file"] {
    width: 180px;
    height: 35px;
    line-height: 35px;
}
.el-icon-close {
    float: right;
    width: 24px;
    height: 24px;
    vertical-align: top;
}

.modal-content button {
    background-color: #0a65cc;
    color: #fff;
    width: 50px;
    height: 33px;
    line-height: 33px;
    border-radius: 3px;
    font-size: 13px;
    font-weight: 600;
}
img{
    width: 450px;
    margin-top: 60px;
}
.service{
    clear: both;
    height: 80px;
    border-radius: 3px;
}
.service ul li{
    width: 47%;
    height: 80px;
    float: left;
    padding-left: 15px;
    margin: 0 10px;
    background-color: #fff;
    border-radius: 5px;
    margin: 10px;
}
.service ul li:hover{
    box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.1);
}
.service ul li i{
    float: left;
    width: 40px;
    height: 40px;
    line-height: 40px;
    margin-top: 18px;
    padding-top: 2px;
    margin-right: 18px;
    color: #0A65CC;
    font-size: 26px;
    background: #E7F0FA;
    border-radius: 2px;
}
.service_txt{
    float: left;
    text-align: left;
}
.service_txt h5,.position h5{
    font-size: 15px;
    font-weight: 600;
    margin-top: 18px;
    color: black;
}
.service_txt p,.position p{
    font-size: 12px;
    color: gray;
}
.two-info{
    height: 225px;
    background-color: #F7F7F8;
}
h3{
    color: black;
    font-size: 29px;
    font-weight: 600;
    text-align: center;
}
// .help{

// }
.two-info .help ul li{
    width: 30%;
    height: 150px;
    float: left;
    padding-top: 15px;
    margin: 25px 10px;
    border-radius: 10px;
    text-align: center;
}
.help ul li:hover{
    background-color: #fff;
}
.help ul li i{
    display: block;
    width: 50px;
    height: 50px;
    margin-left: 40%;
    padding-top: 12px;
    border-radius: 25px;
    font-size: 25px;
    background-color: #fff;
    color: #0A65CC;
}
.help_txt h5{
    font-size: 15px;
    font-weight: 600;
    margin-top: 15px;
    margin-bottom: 8px;
    color: black;
}
.help_txt p {
    font-size: 12px;
}
.three-info{
    height: 255px;
}
.three-info h3,.four-info h3{
    float: left;
}
.three-info button{
    width: 100px;
    height: 40px;
    float: right;
    border: 1px solid #0A65CC;
    border-radius: 3px;
    background-color: #fff;
    color: #0A65CC;
    font-weight: 600;
    font-size: 15px;
}
.position ul li{
    width: 22%;
    height: 80px;
    float: left;
    padding-left: 1%;
    background-color: #fff;
    border-radius: 5px;
    margin: 1% 1% 1% 2%;
}
.position ul li:hover{
    box-shadow: 0px 0px 5px 5px rgba(0, 0, 0, 0.1);
}
.position ul li i{
    float: left;
    width: 40px;
    height: 40px;
    line-height: 40px;
    margin-top: 18px;
    padding-top: 2px;
    margin-right: 18px;
    color: #0A65CC;
    font-size: 26px;
    background: #E7F0FA;
    border-radius: 2px;
}
.position_txt {
    text-align: left;
}
.three-info .hot,.four-info .hot{
    height: 65px;
}
.four-info{
    height: 370px;
    background-color: #fff;
}
.company ul li{
    display: inline-block;
    width: 30%;
    height: 130px;
    margin:10px;
    border-radius: 10px;
    border-bottom: 1px solid lightgray;
    border-left: 1px solid lightgray;
}
.company ul li .el-icon-basketball{
    display: block;
    float: left;
    width: 40px;
    height: 40px;
    line-height: 40px;
    font-size: 20px;
    margin: 18px 15px auto 15px;
    background-color: #EA4C89;
    color: #fff;
    border-radius: 2px;
}
.company ul li span{
    display: inline-block;
    width: 60px;
    height: 18px;
    margin-left: 10px;
    text-align: center;
    background-color: #FCEEEE;
    color: #e05151;
    font-size: 12px;
    border-radius: 10px;
}
.company ul li button{
width: 93%;
height: 40px;
margin:15px auto auto 16px;
background-color: #E7F0FA;
color: #0A65CC;
font-weight: 600;
border-radius: 3px;
}
.six-info{
    height: 110px;
    background-color: #fff;
    text-align: center;
}
.register{
    margin:20px 150px 10px auto;
}
.register .fl,.register .fr{
    width: 27%;
    height: 110px;
    margin-left: 155px;
    border-radius: 3px;
}
.register .fl{
    background-color: #f7f7f8;
}
.register .fr{
    background-color: #E7F0FA;
}
.register .fl h2,.register .fr h2{
    margin: 10px auto 10px auto;
    font-size: 20px;
    font-weight: 600;
}
.register .fl h2{
    color: black;
}
.register .fr h2{
    color: #0A65CC;
}
.register .fl button,.register .fr button{
    width: 150px;
    height: 40px;
    background-color: #fff;
    color: #0A65CC;
    border-radius: 3px;
    border: 1px solid #0A65CC;
    font-size: 15px;
    font-weight: 600;
}
</style>