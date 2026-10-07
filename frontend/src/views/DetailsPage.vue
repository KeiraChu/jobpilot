<template>
    <div class="details">
      <div class="right-container rounded-2xl bg-white px-6 py-6 scrollable-element">
            <header class="flex items-center justify-between">
                <div>
                      <div class="text-hei font-bold text-xl flex items-center space-x-4">
                        <h1 >{{selectedPosition.title}}</h1>
                        <p class="text-red-500">
                          {{selectedPosition.salary}}
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
                <div class="space-x-3.5">
                    <button class="py-2 border-zhuti border px-4 rounded-xl text-sm text-zhuti">
                      感兴趣
                    </button>
                  <button class="py-2 bg-zhuti px-4 rounded-xl text-sm text-white hover:">
                    能力评价
                  </button>
                </div>
              </header>
           <section >
             <p class="text-left mt-8 font-bold">
               职位描述：
             </p>
             <div class="flex space-x-2 mt-3 ">
               <!-- <el-tag type="info" v-for="item in rightContent.jobDescription.tags">
                 {{item}}
               </el-tag> -->
               <el-tag type="info">
                        {{selectedPosition.education }}
                    </el-tag>
             </div>
             <p style="line-height: 30px" class="text-left my-6 text-sm">{{ selectedPosition.description }}
             </p>
           </section>
           <section class="flex items-center border-t border-b py-5">
             <div class="rounded-full w-10 h-10 flex items-center justify-center bg-blue-50 text-zhuti font-bold" aria-hidden="true">招</div>
             <div class="ml-2">
               <p class="font-bold text-left flex space-x-2 items-center">{{selectedPosition.hiring_manager }}
                <span class="text-xs text-hui-100 font-normal">{{selectedPosition.last_active}}</span>
               </p>
               <p class="text-xs text-left mt-1"> {{selectedPosition.company}}</p>
             </div>
           </section>
           <section >
             <p class="text-left mt-8 font-bold">
               职位描述：
             </p>
             <p class="text-left mt-2">
               <span class="text-sm">
                  <i class="iconfont icon-dingwei"></i>
                    {{selectedPosition.address}}
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
    </div>
</template>
<script>
export default {  
  computed: {  
    selectedPosition() {  
      return this.$store.getters.selectedPosition(this.$route.query.id);  
    },  
  },  
  created() {  
    // 您也可以在这里从路由中获取 id 并更新 Vuex store 中的 positionId（如果需要）  
    const id = this.$route.query.id;  
    this.$store.commit('updatePositionId', id);  
  },  
}
</script>

<style scoped>
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
