<template>
<div class="carousel">
  <div class="w">
    <h3>客户感言</h3>
    <el-carousel
      :height="'160px'" 
      :autoplay="false"
      :interval="2500"
      indicator-position="outside"  
      :loop="true"  
      arrow="always"
    >  
      <el-carousel-item v-for="(group, index) in displayedGroups" :key="index">  
        <div class="carousel-group">  
          <div class="carousel-item" v-for="(item, itemIndex) in group" :key="itemIndex">  
            <div class="rate">{{ item.rate }}</div>  
            <div class="text">{{ item.text }}</div>
            <div class="image" aria-hidden="true">{{ item.name.slice(0, 1).toUpperCase() }}</div>
            <div class="intro">
              <h5>{{ item.name }}</h5>
              <p>{{ item.work }}</p>
            </div>
            <i></i>
            <div class="tags">  
              <span v-for="(tag, tagIndex) in item.tags" :key="tagIndex" class="tag">{{ tag }}</span>  
            </div>  
          </div>  
        </div>  
      </el-carousel-item>  
    </el-carousel>
  </div>
</div>
</template>  
<script>  
export default {  
  data() {  
    return {  
      jobs: [  
        // 1
        {
        // 评分
        rate:'',
        text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师', 
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师', 
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      // 2
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师', 
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      // 3
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师', 
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      // 4
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      // 5
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师',  
      },
      {rate:'',
      text:'"很方便，能跟想去的公司HR直接联系，很快能得到结果"',
        img:'',
        name:'fdjjg',
        work:'工程师', 
      },
      ],  
      displayedGroups: [], // 用于存放当前要显示的职位组  
    };  
  },  
  mounted() {  
    this.setupCarousel();  
  },  
  methods: {  
    setupCarousel() {  
      // 将15组数据分为5组，每组3个  
      for (let i = 0; i < this.jobs.length; i += 3) {  
        this.displayedGroups.push(this.jobs.slice(i, i + 3));  
      }  
    },  
  },  
};  
</script>  
<style lang="less" scoped>  
@import '../less/reset.less';
.carousel{
  background-color: #f7f7f8;
}
.w{
  width: 1060px;
}
h3{
    font-size: 28px;
    font-weight: 600;
    color: black;
    text-align: center;
    margin-bottom: 20px;
    padding-top: 15px;
} 
.el-carousel--horizontal {
    overflow: hidden;
    height: 160px;
}
.el-carousel .el-carousel__container {
    position: relative;
    height: 160px;
}
.carousel-group {  
  display: flex;  
  justify-content: space-between;  
  width: 1060px;
  height: 120px;
  padding: 0 40px 0 60px;
}  
.carousel-item {  
  width: 300px;
  height: 130px;  
  overflow: hidden;
  background-color: #fff;
  margin-right: 15px;
} 
/* .rate{

} */
.rate,.text{
  margin: 15px;
  text-align: left;
}
.text{
  font-size: 13px;
}
.image{
  width: 40px;
  height: 40px;
  float: left;
  margin: auto 15px;
  border-radius: 50%;
  background: #e7f6fb;
  color: #1677a8;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}
.intro h5{
  color: black;
  font-size: 14px;
  font-weight: 600;
  text-align: left;
}
.intro p{
  font-size: 12px;
  text-align: left;
}
</style>
