<template>
    <div class="person">
        <div class="userinfo">
            <div class="upload">

            </div>
            <div class="container">
                <div class="headbox">
               <!--  <i class="el-icon-s-custom" style="display: inline-block;width: 35px;height: 35px;font-size: 30px;margin-top: 20px;"></i> -->
               <img src="../assets/image/favicon.png" alt="">
                </div>
                <div class="self">
                    <div class="name">XXX</div>
                    <div class="age">02年</div>
                </div>
                <div class="other-info">
                    <div class="expect">
                        <span>期望:</span>
                    </div>
                    <div class="edu">
                        <span>北京理工大学-机械设计</span>
                        <span class="gray">2020-2024</span>
                    </div>
                </div>
                <div class="resume_btn">
                    <a href="#">在线简历</a>
                </div>
            </div>
        <!-- {{ uesrname }}{{ email }} {{ phone }}{{ degree }}
        {{city_expect}} {{ position_expect }}
        {{ school }} {{ profession }} -->
        </div>
    </div>
</template>
<script>

</script>

<style lang="less" scoped>
.person{
    background: linear-gradient(to bottom, #C9E9F6, #fff);
     
}
.userinfo{
    display: flex;
    justify-content: left; /* 水平居中所有子元素 */  
    align-items: center; /* 垂直居中所有子元素（如果需要） */ 
}
.upload{
    width: 22%;
    height: 55px;
    margin-left: 5%;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid rgba(0,0,0,0.1);
}
.container{
    // display: flex;
    position: relative;
    text-align: left;
    margin: 10px 40px;
    width: 50%;
    background-color: #fff;
    border-radius: 10px;
    border: 1px solid rgba(0,0,0,0.1);
}
.info{
    position: relative;
    width: 75%;
}
.headbox,.self,.other-info{
    display: inline-block;
}
.headbox img{
    width: 35px;
    height: 35px;
    border-radius: 12px;
    margin-left: 15px;
    margin-bottom: -2px;
}
.self{
    margin: 14px 15px 14px 15px;
}
.other-info {
    text-align: left;
    margin: 14px 15px 0 15px;
}
.other-info .edu .gray{
    padding-left: 15px;
    color: gray;
}
.resume_btn{
    position: absolute;
    top: 19px;
    right: 0px;
    background-color: #fff;
    width: 12%;
    height: 47%;
    border: 1px solid rgba(0,0,0,0.1);
}

</style>