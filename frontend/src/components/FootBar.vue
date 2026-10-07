<!-- eslint-disable-next-line vue/multi-word-component-names -->  
<template>
    <div class="footer">
        <!-- 底部模块 -->
    <footer class="footer1">
        <div class="w">
            <ul class="call">
                <li><img src="../assets/image/foot.png" alt=""></li>
                <li>
                    热线: <em class="white">(319)555-0115</em>
                </li>
            </ul>
            <div class="service">
                <dl>
                    <dt class="white">简介</dt>
                    <dd><a href="#">关于我们</a></dd>
                    <dd><a href="#">法律条款</a></dd>
                </dl>
                <dl>
                    <dt class="white">合作</dt>
                    <dd><a href="#">加入我们</a></dd>
                    <dd><a href="#">联系我们</a></dd>
                </dl>
                <dl>
                    <dt class="white">帮助</dt>
                    <dd><a href="#">帮助中心</a></dd>
                    <dd><a href="#">常见问题</a></dd>
                </dl>
                <dl>
                    <dt class="white">服务</dt>
                    <dd><a href="#">职位搜索</a></dd>
                    <dd><a href="#">简历中心</a></dd>
                </dl>
            </div>
        </div>
    </footer>
    <footer class="footer2">
        <div class="w">
            <div class="fl">@2021 Jobpilot - Job Portal.All rights Rserved
            </div>
            <div class="fr">
                <i class="el-icon-share"></i>
                <i class="el-icon-s-promotion"></i>
                <i class="el-icon-question"></i>
                <i class="el-icon-info"></i>
            </div>
        </div>
    </footer>
    </div>
</template>

<style lang="less" scoped>
@import '../less/reset.less';
/* 底部模块 */
.footer1 {
    position: relative;
    height: 190px;
    background-color: #18191c;
    margin-top: 20px;
    padding-top: 60px;
    border: 1px solid #232529;
}

.footer1 .call {
    position: absolute;
    width: 15%;
    top: 15%;
    left: 18%;
}

li {
    color: #6c6b76;
    text-align: left;
}
.white{
    color: #fff;
}
.footer1 .call li:nth-child(2) {
    font-size: 14px;
    margin: 20px 0 10px 0;
}

.footer1 .call img {
    width: 112px;
    height: 28px;
}

.footer1 .service {
    position: absolute;
    width: 45%;
    top: 15%;
    left: 39%;
}

.footer1 .service dt {
    font-size: 15px;
    margin-bottom: 15px;
    text-align: left;
}

.footer1 .service dl {
    float: left;
    width: 11%;
    margin-left: 11%;
}

.footer1 .service dd {
    margin-bottom: 10px;
    text-align: left;
}

.footer1 .service dd a {
    color: #6c6b76;
}

.footer2 {
    color: #6c6b76;
    height: 40px;
    background-color: #18191c;
}

.footer2 .w {
    line-height: 50px;
}

.footer2 .w i {
    color: #767f8c;
}
</style>