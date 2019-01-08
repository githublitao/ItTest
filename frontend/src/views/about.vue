<template>
    <div style="margin-top: 10px">
        <!--<div class="bubble">-->
            <!--<div class="title-font">-->
                <!--由我们：-->
            <!--</div>-->
            <!--<div style="margin-left: 30px">-->
                <!--<div>测试逆鳞提供技术上支持</div>-->
                <!--<div>女司机坑姐提供云服务器</div>-->
                <!--<div>逗逼群主逼逼主页面设计</div>-->
                <!--<div>共同组成了本群官方站点</div>-->
            <!--</div>-->
        <!--</div>-->
        <el-col :span="12">
        <div class="bubble">
            <div class="title-font">
                目的：
            </div>
            <div style="margin-left: 30px">
                <div>为广大群友提供服务信息</div>
            </div>
        </div>
        </el-col>
    <el-col :span="12">
        <div class="bubble">
            <div class="title-font">
                未来：
            </div>
            <div style="margin-left: 30px">
                <div>逐步完善服务性信息内容</div>
            </div>
        </div>
    </el-col>
        <el-col :span="12">
        <div class="bubble">
            <div class="title-font">
                注意：
            </div>
            <div style="margin-left: 30px">
                <div>你在变我在变时间也在变</div>
                <div>所有信息仅供大家来参考</div>
                <div>不保证信息百分百的准确</div>
            </div>
        </div>
        </el-col>
        <el-col :span="12">
        <div class="bubble">
            <div class="title-font">
                Q群：
            </div>
            <div style="margin-left: 30px">
                <div>无论你关注或不关注我们、我们都会在这里不离不弃</div>
                <div>全测试类群最全资料分类、最人性化贴心服务于群友</div>
                <div>599733338、期待你的加入！</div>
            </div>
        </div>
        </el-col>
    </div>
</template>

<script>
/* eslint-disable */
    export default {
        name: "about"
    }
</script>

<style scoped>
    .title-font{
        font-size: 20px;
        margin-bottom: 10px;
        font-weight: bold;
        color: #606266;
    }
    .bubble{
        width: 70%;
        margin: 20px;
        padding: 60px;
        display:  inline-block;
        border:  1px solid #606266;
        border-radius: 30px;
        box-shadow: 5px 5px 5px #606266;
    }

</style>
