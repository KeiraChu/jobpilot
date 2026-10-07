<template>
    <div class="recommend">
        <section class="job-recommend">
     <div class="bg-white py-3">
       <h1 class="text-2xl text-left message-container px-6  font-bold">
         推荐简历
         <button class="py-2 border-zhuti border px-4 rounded-xl text-sm text-zhuti ml-auto" @click="goPublish">
          完善职位信息
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
          <a-select  style="width: 120px" placeholder="期望薪资">
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
          <!-- <a-select  style="width: 120px" placeholder="期望城市">
            <a-select-option value="不限">
              不限
            </a-select-option>
            <a-select-option value="0-20人">
              0-20人
            </a-select-option>
            <a-select-option value="3-5k">
              20-99人
            </a-select-option>
          </a-select> -->
        </div>
       </div>
     </div>
     <section class="message-container mt-4" style="margin-top: 20px;">
         <div class="left-container space-y-4 px-4 scrollable-element">
          <div v-for="(item , index) in leftData" @click="leftActive = index" :class="`bg-hui p-5 rounded-2xl hovershadow-lg cursor-pointer ${leftActive === index ? 'border border-zhuti' : ''}`" :key="index">
                    <p class="flex justify-between">
                      <span class="tex-hei font-bold">{{item.name}}</span>
                      <span class="text-red-500 font-bold">{{item.address}}</span>
                    </p>

                    <div class="flex space-x-2 mt-3 ">
                      <el-tag type="info" v-for="item in item.tag">
                        {{item}}
                      </el-tag>
                    </div>
                    <footer class="flex mt-4 justify-between">
                      <div class="text-sm hover:text-zhuti">
                       <i class="el-icon-user"></i>
                        {{item.title}}</div>
                      <!-- <div class="text-sm">{{item.address}}</div> -->
                    </footer>
                </div>
         </div>
         <div class="right-container rounded-2xl bg-white px-6 py-6 scrollable-element">
            <header class="flex items-center justify-between">
                <div>
                      <div class="text-hei font-bold text-xl flex items-center space-x-4">
                        <h1 >{{rightContent.title}}</h1>
                        <!-- <p class="text-red-500">
                          {{rightContent.price}}
                        </p> -->
                      </div>
                      <!-- <div class="flex space-x-4 mt-1">
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
                      </div> -->
                    </div>
                <div class="space-x-3.5">
                    <button class="py-2 border-zhuti border px-4 rounded-xl text-sm text-zhuti">
                      聊一聊
                    </button>
                  <!-- <button class="py-2 bg-zhuti px-4 rounded-xl text-sm text-white hover:">
                    能力评价
                  </button> -->
                </div>
              </header>
           <section>
             <!-- <p class="text-left mt-8 font-bold">
               职位描述：
             </p>
             <div class="flex space-x-2 mt-3 ">
               <el-tag type="info" v-for="item in rightContent.jobDescription.tags">
                 {{item}}
               </el-tag>
             </div> -->
             <p v-html="rightContent.jobDescription.content" style="line-height: 30px" class="text-left my-6 text-sm">
             </p>
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
let leftData = [
  {
    id:1,
    title:'Java开发工程师',
    price:'8-10k',
    tag:['有项目经验','本科','myeclipse','java'],
    name:'湖科',
    address:'上海科技信息大学',
    jobDescription:{
    tags:['有项目经验','本科','myeclipse','java'],
    content:'<img src="/工程师2.webp" alt="Java开发工程师职位描述" style="width: 100%; height: auto;">'
    }

  },
  {
    id:2,
    title:'Java开发工程师',
    price:'6-8k',
    tag:['有项目经历','工作经验','本科','eclipse','Myeclipse','Bootstrap','ajax'],
    name:'湖科',
    address:'上海科技信息大学',
    jobDescription:{
      tags:['有项目经历','工作经验','本科','eclipse','Myeclipse','Bootstrap','ajax'],
    content:'<img src="/gcs5.webp" alt="Java开发工程师职位描述" style="width: 100%; height: auto;">'
    }

  },
  {
    id:3,
    title:'JAVA初级工程师',
    price:'2-5k',
    tag:['有项目经历','工作经验','本科','数据库','java编程'],
    name:'湖科',
    address:'广州大学',
    jobDescription:{
      tags:['有项目经历','工作经验','本科','数据库','java编程'],
    content:'<img src="/gcs.webp" alt="Java开发工程师职位描述" style="width: 100%; height: auto;">'
    }

  },
  {
    id:4,
    title:'JAVA、HTML5开发实习生',
    price:'2-4k',
    tag:['4年经验','实习经验','工作经验','本科','java','Pascal'],
    name:'湖科',
    address:'上海科技信息大学',
    jobDescription:{
      tags:['4年经验','实习经验','工作经验','本科','java','Pascal'],
    content:'<img src="/sxs.webp" alt="Java开发工程师实习生职位描述" style="width: 100%; height: auto;">'
    }

  },
  {
    id:5,
    title:'Java架构师 (MJ000147)',
    price:'40-70K·15薪',
    tag:['有项目经历','工作经验','本科','nginx','fastcgi'],
    name:'湖科',
    address:'上海科技信息大学',
    jobDescription:{
      tags:['有项目经历','工作经验','本科','nginx','fastcgi'],
      content:'<img src="/gcs4.webp" alt="Java开发工程师职位描述" style="width: 100%; height: auto;">'
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
      texts: ['非常不满意', '不满意', '一般', '满意', '惊喜']
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
    goPublish(){
        this.$store.dispatch('setActiveMenuItem', '2');
        this.$router.push("/publish").catch((err) => err);
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
  // 从本地存储获取 activeIndex  
  const savedIndex = localStorage.getItem('activeIndex');  
  if (savedIndex) {  
    // 如果存在，则使用保存的 activeIndex  
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
/* 隐藏滚动条但允许滚动 */
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
