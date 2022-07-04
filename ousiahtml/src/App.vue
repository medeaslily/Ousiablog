<template>
  <div id="app">
    <!-- 头部导航 -->
    <div id="top-menu" class="dweb"></div>
    <!-- 侧边栏 左-导航 -->
    <div id="left-menu" :class="'dweb ' +mobile_left">
      <i @click="showHideLeftMenu" id="left-btn" class="el-icon-s-fold"></i>
      <!-- 导航栏 -->
      <el-col :span="24" style="margin-top:80px">
        <!-- 启用router -->
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#00000000"
          router
          @select="chooseMenu"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-folder-opened"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/add-article">发布文章</el-menu-item>
              <el-menu-item index="/article-list">文章列表</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="2">
            <i class="el-icon-user-solid"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-menu-item index="3">
            <i class="el-icon-money"></i>
            <span slot="title">打赏记录</span>
          </el-menu-item>
          <el-menu-item index="4">
            <i class="el-icon-s-operation"></i>
            <span slot="title">栏目管理</span>
          </el-menu-item>
          <!-- 像使用data一样直接使用computed的函数 -->
          <el-menu-item v-if="authUserLogin" @click="blogLogout()" index="5">
            <i class="el-icon-back"></i>
            <span slot="title">退出登录</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
    <!-- 页面内容 -->
    <div id="content" :class="mobile_content">
      <router-view :screenWidth="screenWidth"></router-view>

      <div id="footer" class="dweb">
        <span>Copyright © 2022 狄奥尼索斯之冠</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 屏幕宽度
      screenWidth: document.body.clientWidth,
      // 特定的样式保存在mobile
      mobile_left: "",
      mobile_content: "",
    };
  },
  //计算属性的 getter 函数是没有副作用 (side effect) 的，这使它更易于测试和理解
  computed: {
    //返回用户状态
    authUserLogin() {
      //使用全局变量直接调用getters的函数来获取state（token）
      return this.$store.getters.isnotUserlogin;
    },
  },
  //监听函数
  watch: {
    //当authUserLogin的返回值发生变化（token被删除为null）就跳转到登陆页面
    authUserLogin(curVal) {
      if (curVal == null) {
        this.$router.push({ path: "/login" });
      }
    },
  },
  //created是在mouted之前的生命周期的环节
  created() {
    //在较早的一个生命周期created里调用自动登录函数
    this.$store.dispatch("tryAutoLogin");
  },
  //mouted是打开第一个页面执行的最后一个函数的生命周期环节
  mounted() {
    // 动态实时获取屏幕宽度
    // window.onresize=()=>{
    //   this.screenWidth = document.body.clientWidth
    //   console.log(this.screenWidth)
    // }
    this.changeDevice();
  },
  methods: {
    // 发布文章
    chooseMenu(index) {
      //console.log(index);
      this.$router.push({ path: index });
    },
    // 为不同的屏幕宽度配置不同的样式
    changeDevice() {
      if (this.screenWidth <= 500) {
        // ’xs‘来自Element，作为响应式布局的参数，代表某一种机型
        this.mobile_left = "xs";
        this.mobile_content = "xs";
      }
    },
    // 实现icon的切换mobile功能
    showHideLeftMenu() {
      if (this.mobile_left == "") {
        this.mobile_left = "xs";
      } else {
        this.mobile_left = "";
      }
      // 宽屏
      if (this.screenWidth > 500) {
        if (this.mobile_content == "xs") {
          this.mobile_content = "";
        } else {
          this.mobile_content = "xs";
        }
      }
    },
    //退出登录
    blogLogout() {
      this.$store.dispatch("blogLogout", this.$store.getters.isnotUserlogin);
    },
  },
};
</script>

<style>
.el-col {
  margin-top: 5px;
}
</style>
