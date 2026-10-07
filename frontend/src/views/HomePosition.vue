<template>
  <div class="position">
    <section class="job-recommend">
     <div class="bg-white py-3">
       <h1 class="text-2xl text-left message-container px-6  font-bold">
         推荐职位
         <button class="py-2 border-zhuti border px-4 rounded-xl text-sm text-zhuti ml-auto" @click="goToAboutView">
          完善简历
        </button>
       </h1>
       <div  class="message-container px-6 flex justify-between items-center">
        <div class="space-x-4">
          <a-select style="width: 120px" placeholder="求职类型">
            <a-select-option value="不限">
              不限
            </a-select-option>
            <a-select-option value="全职">
              全职
            </a-select-option>
            <a-select-option value="兼职">
              兼职
            </a-select-option>
            <a-select-option value="实习">
              实习
            </a-select-option>
          </a-select>
          <a-select  style="width: 120px" placeholder="工作经验">
            <a-select-option value="不限">
              不限
            </a-select-option>
            <a-select-option value="在校生">
              在校生
            </a-select-option>
            <a-select-option value="应届生">
              应届生
            </a-select-option>
            <a-select-option value="经验不限">
              经验不限
            </a-select-option>
            <a-select-option value="1年以内">
              1年以内
            </a-select-option>
            <a-select-option value="1-3年">
              1-3年
            </a-select-option>
            <a-select-option value="3-5年">
              3-5年
            </a-select-option>
            <a-select-option value="5-10年">
              5-10年
            </a-select-option>
            <a-select-option value="10年以上">
              10年以上
            </a-select-option>
          </a-select>
          <a-select  style="width: 120px" placeholder="学历要求">
            <a-select-option value="不限">
              不限
            </a-select-option>
            <a-select-option value="高中及以下">
              高中及以下
            </a-select-option>
            <a-select-option value="大专">
              大专
            </a-select-option>
            <a-select-option value="本科">
              本科
            </a-select-option>
            <a-select-option value="研究生">
              研究生
            </a-select-option>
            <a-select-option value="博士">
              博士
            </a-select-option>
          </a-select>
          <a-select  style="width: 120px" placeholder="薪资待遇">
            <a-select-option value="不限">
              不限
            </a-select-option>
            <a-select-option value="3k以下">
              3k以下
            </a-select-option>
            <a-select-option value="3k-5k">
              3k-5k
            </a-select-option>
            <a-select-option value="5k-10k">
              5k-10k
            </a-select-option>
            <a-select-option value="10k-20k">
              10k-20k
            </a-select-option>
            <a-select-option value="20k-50k">
              20k-50k
            </a-select-option>
            <a-select-option value="50k以上">
              50k以上
            </a-select-option>
          </a-select>
          <el-cascader
                        class="select"
                        size="medium "
                        :options="options"
                        placeholder="期望城市"
                        v-model="selectedOptions"
                        @change="handleChange"
                        style="width: 120px;"
                    >
                    </el-cascader>
        </div>
       </div>
     </div>
     <section class="message-container mt-4" style="margin-top: 20px;">
         <div class="left-container space-y-4 px-4 scrollable-element">
          <div v-for="(item, index) in reversedLeftData" @click="leftActive = index" :class="`bg-hui p-5 rounded-2xl hovershadow-lg cursor-pointer ${leftActive === index ? 'border border-zhuti' : ''}`" :key="item.id">
                    <p class="flex justify-between">
                      <span class="tex-hei font-bold">{{item.title}}</span>
                      <span class="text-red-500 font-bold">{{item.price}}</span>
                    </p>
                    <div class="flex space-x-2 mt-3 ">
                      <el-tag type="info" v-for="tag in item.tag" :key="tag">{{tag}}</el-tag>
                    </div>
                    <footer class="flex mt-4 justify-between">
                      <div class="text-sm hover:text-zhuti">
                       <i class="el-icon-office-building"></i>
                        {{item.name}}</div>
                      <div class="text-sm">{{item.address}}</div>
                    </footer>
          </div>
          </div>
         <div class="right-container rounded-2xl bg-white px-6 py-6 scrollable-element">
            <header class="flex items-center justify-between">
                <div>
                      <div class="text-hei font-bold text-xl flex items-center space-x-4">
                        <h1 >{{rightContent.title}}</h1>
                        <p class="text-red-500">
                          {{rightContent.price}}
                        </p>
                      </div>
                      <div class="flex space-x-4 mt-1">
                        <span class="text-sm">
                        <i class="iconfont icon-dingwei"></i>
                          地点
                      </span>
                        <span class="text-sm">
                        <i class="iconfont icon-gongzuotai"></i>
                          经验不限
                      </span>
                        <span class="text-sm">
                        <i class="iconfont icon-xueli"></i>
                          经验不限
                      </span>
                      </div>
                    </div>
                <div class="space-x-3.5" style="display: flex;align-items: center;">
                    <button class="py-2 border-zhuti border px-4 rounded-xl text-sm text-zhuti">
                      聊一聊
                    </button>
                  <button class="py-2 bg-zhuti px-4 rounded-xl text-sm text-white hover:" @click="gotoAssess">
                    能力评价
                  </button>
                </div>
              </header>
           <section>
             <p class="text-left mt-8 font-bold">
               职位描述：
             </p>
             <div class="flex space-x-2 mt-3 ">
              <el-tag type="info" v-for="item in rightContent.jobDescription.tags">{{ item }}</el-tag>
             </div>
             <p v-html="rightContent.jobDescription.content" style="line-height: 30px" class="text-left my-6 text-sm">
             </p>
           </section>
           <section class="flex items-center border-t border-b py-5">
             <div class="rounded-full w-10 h-10 flex items-center justify-center bg-blue-50 text-zhuti font-bold" aria-hidden="true">招</div>
             <div class="ml-2">
               <p class="font-bold text-left flex space-x-2 items-center">刘先生
                <span class="text-xs text-hui-100 font-normal">刚刚活跃</span>
               </p>
               <p class="text-xs text-left mt-1"> 诺鑫网络科技 · 老板 </p>
             </div>
           </section>
           <section >
             <p class="text-left mt-8 font-bold">
               职位描述：
             </p>
             <p class="text-left mt-2">
               <span class="text-sm">
                  <i class="iconfont icon-dingwei"></i>
                    承德双桥区天泽嘉园A座1-1101室
                </span>
             </p>
             <footer>
               <div class="map">地图位置：{{ rightContent.address || '暂无详细地址' }}</div>

               <button class="py-2 border-zhuti border px-8 rounded-xl text-sm text-zhuti">
                 查看更多信息
               </button>
             </footer>
           </section>
         </div>
     </section>
     <div class="right" style="position: fixed;top: 160px;right: 10px;border: 2px solid rgb(104, 202, 237);background-color: #fff;border-radius: 20px;padding: 10px 6px;">
      <div style="float: right;">
        <h1 style="font-weight: 600;">推荐评价</h1>
            <el-rate v-model="value" :show-text="true" :texts="texts" style="display: inline-block; margin: 10px 0">
          </el-rate><br>
            <a-input style="width: 192px;margin-bottom: 10px" placeholder="请输入您对推荐结果的评价" v-model="rate"/><br>
          <button class="py-2 bg-zhuti px-4 rounded-xl text-sm text-white hover:" @click="reverseData">
            重新推荐
                  </button>
          </div>
     </div>
    </section>
  </div>
   
</template>

<script>
import { regionData} from "element-china-area-data";
let leftData=[
  {
    id:1,
    title:'Java开发工程师（实习）',
    price:'2-4k',
    tag:['1-3年','大专','SpringMVC','SpringBoot','spring cloud'],
    name:'湖北致慧信息技术有限公司',
    address:'宜昌西陵区宜昌国家高新区创新创业服务中心603',
    jobDescription:{
      tags:['1-3年','大专','SpringMVC','SpringBoot','spring cloud微服务框架'],
      content:'岗位要求：<br/>'+
          '1、大专及以上学历，计算机或相关专业优先；<br/>' +
          '2、具有一定的Java基础，数据结构、多线程、IO操作等；<br/>'+
          '3、熟悉SpringMVC、SpringBoot框架，熟悉spring cloud微服务框架；<br/>'+
          '4、掌握Oracle、Mysql、SQLServer等关系型数据库中至少一种；<br/>'+
          '5、熟悉XML、HTML/XHTML、CSS、Javascript、AJAX、JSON等Web页面技术有前端框架使用者优先；<br/>'+
          '6、能承受一定的压力，工作认真负责，善于学习总结。<br/>'+
          '岗位职责：<br/>'+
          '1、按照项目需求，完成开发工作；<br/>' +
          '2、完成相关文档编写的工作；<br/>' +
          '3、参与测试、修改关工作；<br/>' +
          '4、参与软件可靠性维护等工作。<br/>' 
    }
  },
  {
    id:2,
    title:'Java开发工程师',
    price:'2-5k',
    tag:['大专','Java','linux','mysql','Spring'],
    name:'北京维联众诚科技有限公司',
    address:'邯郸丛台区邯郸国际会展中心555',
    jobDescription:{
      tags:['大专','Java','linux','mysql','Spring'],
      content:'职位要求：1.java基础扎实，熟练掌握java的注解，java内存机制，java多线程。2.熟练使用linux，redis、mysql。3.熟练掌握Spring、Springboot、Mybatis。4.熟练掌握Html、CSS、bootstrap、jquery、Vue等前端技术。5.具有较强的逻辑思维能力和沟通能力。6.踏实勤奋，追求上进。<br/>'
    }

  },{
    id:3,
    title:'JAVA初级工程师',
    price:'2-5k',
    tag:['1-2年','大专','后端服务的开发','Maven','Spring'],
    name:'肇庆云虫科技有限公司',
    address:'肇庆端州区星湖湾C区街铺，仁心医院旁',
    jobDescription:{
      tags:['1-2年','大专','后端服务的开发','Maven','Spring'],
      content:'1、参与产品的需求分析讨论，完成系统设计；2、负责公司产品后端服务的开发工作，并完成单元测试；4、负责相关模块的性能分析及改进，保证系统的稳定性；5、负责现有系统的维护工作；6、负责相关技术文档的编写；任职资格：1、计算机或相关专业，1-2年Java开发工作经验；2、熟练使用Java、Maven、PowerDesigner。3、熟悉后端springMVC、springboot、mybatis、redis；5、熟练掌握至少一种主流数据库MySQL、Oracle或其他关系型数据库，能编写高质量的sql脚本，有数据库优化、SQL优化经验优先；6、有分布式、高并发、高负载、高可用性系统的设计开发经验者优先；7、有较强的业务理解能力，善于团队合作，执行力强，能承受工作压力，有较强的责任心和上进心；8、有微信小程序工作经验优先。9、工作地点：广东省肇庆市端州区，<br/>'
    }

  },{
    id:4,
    title:'JAVA、HTML5开发实习生',
    price:'2-4k',
    tag:['大专','JSON','HTML5','MyBatis'],
    name:'广州非格科技有限公司',
    address:'广州黄埔区广州非格科技有限公司3栋504房',
    jobDescription:{
      tags:['大专','JSON','HTML5','MyBatis'],
      content:'1、计算机相关专业；2、熟悉Java基础和编码规范，熟悉掌握Socket、多线程、文档操作、Xml、JSON等相关技术；3、熟悉HTML,CSS3,Javascript,Ajax等前端开发技术；4、了解或使用过Angular、Vue、jQuery、Bootstrap等前端框架；5、了解HTML5、ES6特性和最新规范，有WebApp开发经验者优先；6、熟悉Mysql或Oracle数据库的使用，具有良好的sql设计和编写能力；7、了解Spring、SpringMVC、MyBatis等框架使用；8、了解至少一种WEB服务器（Tomcat、WebLogic、Apache等）的使用。9、熟悉Eclipse、DreamWeaver、Photoshop等的使用。10、有HTML5移动端前端开发经验者优先；<br/>'
    }
  },{
    id:5,
    title:'Java架构师 (MJ000147)',
    price:'40-70K·15薪',
    tag:['大专','linux','mysql/sqlserver','系统架构设计'],
    name:'跨越速运集团有限公司',
    address:'深圳宝安区跨越新科技总部大楼2楼',
    jobDescription:{
      tags:['大专','linux','mysql/sqlserver','系统架构设计'],
      content:'岗位职责1、主导或者参与系统架构、设计、核心代码开发、系统优化等工作。2、对系统的发展进行规划并推进实施。3、与产品经理一起梳理业务规则，并讨论业务场景实现，并做出有预见性的技术实现方案。4、对现有系统不足进行分析，找到瓶颈，重构优化实现或改进系统架构。任职要求1、专科及以上学历，计算机相关专业，具备五年及以上互联网技术开发经验，担任过架构师并领导过复杂系统的开发、重构。2、具有高并发、海量数据的分布式系统开发经验。3、熟练掌握mysql、memcached，redis等主流数据存储系统，可对系统进行性能调优。4、熟悉linux环境java/php/C#至少一门语言开发。5、熟悉mysql/sqlserver，nosql等。6、有消息中间件、缓存系统、业务监控经验者优先。7、有处理过千万级别的系统经验者优先。8、有分布式、高并发、高可用性、高稳定性、复杂业务处理的经验优先。9、具备模块或子系统的架构设计能力,掌握常见的架构设计方法和模式，理解大型网站所需要用到的架构和技术。10、良好的代码编写、单元测试、注释以及文档的习惯，具备辅导他人的能力和技能。11、 优秀的学习能力,具有专研精神。<br/>'
    }

  }, {
    id:6,
    title:'java后端工程师',
    price:'2-7k',
    tag:['大专','数据库','测试','SpringMVC','Mybatis'],
    name:'北京尔希科技有限公司',
    address:'焦作山阳区焦作市5G产业园二层',
    jobDescription:{
      tags:['大专','数据库','测试','SpringMVC','Mybatis'],
      content:'一、岗位职责：1、根据系统详细设计说明书进行代码实现；2、按公司规范负责实现所承担的业务模块的开发工作。3、实现业务模块的开发，按时完成编码任务，对代码质量负责；4、按规范设计测试用例，进行单元测试，集成测试，并书写测试报告；5、参与技术方案可行性报告和解决方案编写；6、协助其它开发工程师工作。 二、任职要求：1、 计算机科学与技术、软件工程、数学等相关专业，本科以上学历，在校有相关技术开发实践项目经验；2、 熟悉J2EE常用技术，熟悉Spring、SpringMVC、Mybatis、Dubbo、SpringCloud等开源框架，熟悉JQuery,Mvvm模块化前端技术等，了解TOMCAT、JBOSS等应用服务器；3、 熟悉PostgreSQL、MySQL、SQLite、SQL Server数据库之一，能够独立完成简单的SQL查询语句的编写；4、 有良好的沟通和学习能力，强烈的工作责任心和良好的团队协作能力；5、 认同新意发展目标和核心理念，对软件开发有深厚的兴趣，喜欢钻研技术，乐于接受工作挑战。<br/>'
    }

  },
]
export default {
  data(){
    return{
      leftActive:0,
      leftData,
      isReversed: false, 
      originalIndices: null,
      center: {lng: 0, lat: 0},
      zoom: 3,
      value: null,
      texts: ['非常不满意', '不满意', '一般', '满意', '惊喜'],
      options: regionData,
      selectedOptions: [],
    }
  },
  components: {
  },
  methods:{
    reverseData() {  
    setTimeout(() => {  
    this.$nextTick(() => {
      this.isReversed = !this.isReversed;  
    if (this.isReversed) {  
      this.originalIndices = this.leftData.reduce((acc, item, index) => ({  
        ...acc,  
        [item.id]: index  
      }), {});  
      this.leftData.sort((a, b) => b.id - a.id);  
      this.leftActive = 0;  
    } else { 
      const sortedIndices = Object.values(this.originalIndices).sort((a, b) => a - b);  
      this.leftData = sortedIndices.map(index => this.leftData[index]);  
      this.originalIndices = null; // 清除原始索引映射  
    }  
    });  
  }, 2000);
  }, 
    gotoAssess(){
      this.$store.dispatch('setActiveMenuItem', '4');
      this.$router.push('/assess'); 
    },
    goToAboutView() {
      this.$store.dispatch('setActiveMenuItem', '2');
      this.$router.push('/about'); 
    },
    handler ({BMap, map}) {
      this.center.lng = 116.404
      this.center.lat = 39.915
      this.zoom = 15
    }
  },
  computed:{  
    reversedLeftData() {  
    return this.isReversed ? this.leftData : [...this.leftData];  
  }, 
  rightContent() {  
    return this.reversedLeftData[this.leftActive]
  }
  },  
  created() {  
  const savedIndex = localStorage.getItem('activeIndex');  
  if (savedIndex) {  
    this.$store.dispatch('setActiveMenuItem', savedIndex);  
  }  
}
}
</script>
<style>
.job-recommend{
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: #f0f0f0;
}
.message-container{
  margin: 0 auto;
  width: 70%;
  flex: 1;
  display: flex;
  overflow: hidden;
}

.left-container{
  overflow-y: auto;
  width: 40%;
  margin-right: 10px;
}
.right-container{
  overflow-y: auto;
  width: 60%;
}
.bg-hui:hover .tex-hei {
  color: #0a65cc; /* 鼠标悬停时，.tex-hei 文字颜色变为蓝色 */
}
.scrollable-element::-webkit-scrollbar {
  display: none; /* 隐藏滚动条 */
}

.scrollable-element {
  overflow-y: scroll; /* 允许垂直滚动 */
}

.map {
  width: 100%;
  height: 200px;
  margin: 20px 0px;
}

</style>
