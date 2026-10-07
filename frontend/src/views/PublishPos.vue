<template>
    <div class="resume">
      <div class="resume-box">
        <div class="left">
          <div class="upload">
        <i class="el-icon-s-custom" style="display: inline-block;width: 35px;height: 35px;font-size: 30px;margin-top: 20px;"></i>
        <br>
      </div>
      <el-menu
        default-active="2"
        class="el-menu">
        <el-menu-item index="1">
          <a href="#basic"><span slot="title">基本信息</span></a>
        </el-menu-item>
        <el-menu-item index="2">
          <a href="#pos"><span slot="title">职位描述</span></a>
        </el-menu-item>
        <el-menu-item index="3">
          <a href="#salary"><span slot="title">薪资详情</span></a>
        </el-menu-item>
        <el-menu-item index="4">
          <a href="#company"><span slot="title">公司详情</span></a>
        </el-menu-item>
      </el-menu>
        </div>
      <section class="form py-8">
      <h1 class="text-left text-xl font-bold">职位信息</h1>
      <section class="mt-4">
        <a-row :gutter="[30,30]" id="basic">
          <a-col :span="6">
            <p class="text-left">名称</p>
            <a-input class="mt-2" placeholder="请输入名称" v-model="posname"/>
          </a-col>
          
          <a-col :span="6">
            <p class="text-left">类型</p>
            <a-select placeholder="请选择类型" class="w-full mt-2" v-model="type">
              <a-select-option value="销售">销售</a-select-option>
              <a-select-option value="服务业">服务业</a-select-option>
              <a-select-option value="供应链/物流">供应链/物流</a-select-option>
              <a-select-option value="运营">运营</a-select-option>
              <a-select-option value="传媒">传媒</a-select-option>
              <a-select-option value="教育培训">教育培训</a-select-option>
              <a-select-option value="人力/财务/行政">人力/财务/行政</a-select-option>
              <a-select-option value="市场">市场</a-select-option>
              <a-select-option value="设计">设计</a-select-option>
            </a-select>
          </a-col>
          <a-col :span="6">
            <p class="text-left">经验要求</p>
            <a-input class="mt-2" placeholder="eg:1-3年" v-model="workexperience"/>
          </a-col>
          <a-col :span="6">
            <p class="text-left">学历要求</p>
            <a-select placeholder="请选择" class="w-full mt-2" v-model="edu">
              <a-select-option value="硕士及以上">硕士及以上</a-select-option>
              <a-select-option value="本科">本科</a-select-option>
              <a-select-option value="大专">大专</a-select-option>
              <a-select-option value="中专">中专</a-select-option>
              <a-select-option value="不限">不限</a-select-option>
            </a-select>
          </a-col>
        </a-row>

        <a-row :gutter="[30,30]" id="salary">
          <a-col :span="12">
            <p class="text-left">薪资</p>
              <a-input-group compact style="display: flex;justify-content: start;" class="mt-2">
                <a-input style="width: 40%; text-align: center" placeholder="最低薪资" v-model="salary_expect_low"/>
                <a-input
                    style="width: 20%; border-left: 0; pointer-events: none; backgroundColor: #fff;"
                    placeholder="~" disabled
                />
                <a-input
                    style="width: 40%; text-align: center; border-left: 0;"
                    placeholder="最高薪资"
                    v-model="salary_expect_up"
                />
              </a-input-group>
          </a-col>
          <a-col :span="12">
            <p class="text-left">工作地址</p>
            <div class="select">
              <el-cascader
                          class="w-full mt-2"
                          size="small"
                          placeholder="请选择地址"
                          :options="options"
                          v-model="selectedOptions"
                          @change="handleChange"
                      >
                      </el-cascader>
            </div>
          </a-col>
        </a-row>
      </section>
      <h1 class="text-left text-xl font-bold mt-7 mb-4" id="pos">职位描述</h1>
      <el-input type="textarea" :rows="6" v-model="skill" />
      <h1 class="text-left text-xl font-bold mt-7 mb-4" id="salary">薪资详情</h1>
      <el-input type="textarea" :rows="3" v-model="salary" />
      <h1 class="text-left text-xl font-bold mt-7 mb-4" id="company">公司详情</h1>
      <section class="text-left space-y-4">
        <div class="p-4 border rounded-lg cursor-pointer" v-for="(item , index ) in  data1" :key="index" >
          <div class="flex justify-between"  @click="item.isDown = !item.isDown">
            <h1 class="text-base font-bold">{{item.name}}</h1>
            <div>
              <i :class="`${!item.isDown  ? 'el-icon-arrow-down' : 'el-icon-arrow-up'} `"></i>
            </div>
          </div>
          <p class="mt-1">
            <span>{{item.zhiwei}}</span>
            <span class="px-4">|</span>
            <span>{{item.time}}</span>
          </p>
          <div :class="`${!item.isDown ? 'h-0' : 'h-full pt-5'}  overflow-hidden ` ">
            <a-row :gutter="[30,30]">
              <a-col :span="8">
                <p class="text-left">公司名称</p>
                <a-input class="mt-2" placeholder="请输入公司名称" v-model="company_name"/>
              </a-col>
              <a-col :span="8">
                <p class="text-left">企业类型</p>
                <a-select placeholder="请选择企业类型" class="w-full mt-2" v-model="company_type">
                  <a-select-option value="有限责任公司">有限责任公司</a-select-option>
                </a-select>
              </a-col>
              <a-col :span="8">
                <p class="text-left">经营状态</p>
                <a-select placeholder="请选择经营状态" class="w-full mt-2" v-model="running_type">
                  <a-select-option value="存续">存续</a-select-option>
                </a-select>
              </a-col>
            </a-row>
            <a-row :gutter="[30,30]">
                <a-col :span="8">
                <p class="text-left">法定代表人</p>
                <a-input class="mt-2" placeholder="请输入法定代表人姓名" v-model="fdname"/>
                </a-col>
              <a-col :span="8">
                <p class="text-left">成立日期</p>
                <a-month-picker placeholder="请选择时间" class="w-full mt-2" v-model="date"/>
              </a-col>
              <a-col :span="8">
                <p class="text-left">投资资金</p>
                <a-input class="mt-2" placeholder="请输入投资资金" v-model="touzi"/>
                </a-col>
            </a-row>
            <a-row :gutter="[30,30]">
              <a-col :span="24">
                <p class="text-left">公司介绍</p>
                <el-input type="textarea" :rows="5" v-model="education_experience.experience" class="mt-2"/>
              </a-col>
            </a-row>
          </div>
        </div>
      </section>
      <button @click="goPosition">完成</button>
      </section>
      </div>
    </div>
  </template>
  <script>
  import axios from 'axios';
  import { regionData} from "element-china-area-data";
  import {selectPosition }from "../api/position";
  export default {
    data() {
      return {
        username:"",
        email:"",
        phone:"",
        wx:"",
        position_expect: "",
        salary_expect_low: "",
        salary_expect_up: "",
        sex: "",
        start_work_time: "",
        birthday: "",
        city_expect: "",
        from: "",
        political_status: "",
        skill: "1、根据系统详细设计说明书进行代码实现；2、按公司规范负责实现所承担的业务模块的开发工作。3、实现业务模块的开发，按时完成编码任务，对代码质量负责；4、按规范设计测试用例，进行单元测试，集成测试，并书写测试报告；5、参与技术方案可行性报告和解决方案编写；6、协助其它开发工程师工作。",
  
        education_experience: {
          school: "",
          degree: "",
          start_time: "",
          end_time: "",
          profession: "",
          experience: "",
        },
  
        work_experience: {
          company: "",
          position_kind: "",
          start_time: "",
          end_time: "",
          experience: "",
        },
  
        project_experience: {
          project: "",
          role: "",
          start_time: "",
          end_time: "",
          experience: "",
        },
  
        options: regionData,
        selectedOptions: [],
        showModal: false,
        file: null,
        data1:[
          {
            name:'工商信息',
            zhiwei:'工商信息',
            time:'公司介绍',
            isDown:false
          },
        ],
        data2:[
          {
            name:'工作经历',
            zhiwei:'公司名称',
            time:'职位类型',
            isDown:false
          },
         
        ],
        data3:[
          {
            name:'项目经历',
            zhiwei:'项目名称',
            time:'项目角色',
            isDown:false
          },
        ],
        form: {
          content: '',
        },
        customToolbar: [
          ["bold", "italic", "size", " font", "underline", "color", "italic", "strike", "clean",],
          [{ align: ['', 'center', 'right', 'justify'] }],
          [{
            header: [false, 1, 2, 3, 4, 5, 6]
          }],
          [{
            list: "ordered"
          }, {
            list: "bullet"
          }],
          [{
            indent: "-1"
          }, {
            indent: "+1"
          }],
          ["image"],
        ],
      }
    },
    components: {
    },
    
    methods: {
      handleChange(value) {
      },
      handleImageAdded: function (file, Editor, cursorLocation, reseter) {
        var formData = new FormData();
        formData.append("image", file);
        $http.post(this.$common.baseUrl + "upload/image", formData).then(res => {
          let data = res.body;
          if (data.code == 200) {
            let url = data.data.url;
            Editor.insertEmbed(cursorLocation, "image", url);
            resetUploader();
          } else { }
        })
      },
      goMbti(){
        window.location.href = 'https://www.16personalities.com/ch/%E4%BA%BA%E6%A0%BC%E6%B5%8B%E8%AF%95';
      },
      goPosition() {
    setTimeout(() => {
      this.$router.push('/position');
    }, 5000);
  },
      // uploadResume(){
      //   if (this.username == "") {
      //     alert("姓名不能为空");
      //     return;
      //   } else if (this.email == "") {
      //     alert("邮箱不能为空");
      //     return;
      //   } else if (this.phone == "") {
      //     alert("手机号不能为空");
      //     return;
      //   } else if (this.wx == "") {
      //     alert("微信不能为空");
      //     return;
      //   }
      //   else {
      //     axios({
      //       method: "post",  
      //       url: `http://127.0.0.1:4523/m1/3936784-0-default/resume/update`,  
      //     }).then((res) => {  
      //       console.log("简历响应:", res);  
      //     }).catch((error) => {  
      //       console.error("简历出错:", error);
      //     })
      //   }
      // },
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
    created() {  
    // 从本地存储获取 activeIndex  
    const savedIndex = localStorage.getItem('activeIndex');  
    if (savedIndex) {  
      // 如果存在，则使用保存的 activeIndex  
      this.$store.dispatch('setActiveMenuItem', savedIndex);  
    }  
  },
  
  }
  </script>
  <style scoped>
  .resume-box{
    display: flex;
  }
  .left{
    width: 10%;
    margin-left: 8%;
  }.right{
    width: 14%;
    margin-right: 3%;
  }
  .right .mbti{    
    width: 100%;
    height: 7%;
    margin: 30% auto auto 15%;
    border-radius: 4px;
    border: 1px solid #0a65cc;
  }
  .el-icon-thumb{
    margin-top: 6%;
    font-size: 25px;
    color: #0a65cc;
    font-weight: 600;
  }
  .mbti button{
    background-color: #0a65cc;
      color: #fff;
      font-weight: 600;
      margin-top: 4px;
      height: 25px;
      font-size: 13px;
      width: 90px;
  }
  .py-8{
    padding-top: 0px !important;
  }
  
  .upload{
  width: 73%;
  }
  .upload img{
    margin-left: 43%;
    margin-top: 10%;
    border-radius: 4px;
  }
  .upload button{
    background-color: #0a65cc;
      color: #fff;
      width: 80px;
      height: 22px;
      border-radius: 3px;
      font-size: 12px;
      font-weight: 500;
      margin-top: 10px;
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
  .container{
    margin-top: 7%;
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
      height: 35px;
      line-height: 35px;
      border-radius: 3px;
      font-size: 13px;
      font-weight: 600;
  }
  .el-menu{
    width: 20%;
    position: sticky;  
    top: 10%; 
    border: none;
  }
  .form{
    /* margin: 0 auto; */
    width: 65%;
    height: 100%;
  }
  button {
      background-color: #0a65cc;
      color: #fff;
      width: 110px;
      height: 40px;
      border-radius: 3px;
      font-size: 17px;
      font-weight: 600;
      margin-top: 27px;
  }
  .select .el-input__inner:hover{
    border: #0a65cc;
  }
  </style>
