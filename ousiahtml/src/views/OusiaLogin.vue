<template>
  <div id="login-page">
    <div class="dweb loginbox">
      <div class="header">
        用户登录
        <!-- 分割线 -->
        <el-divider></el-divider>
      </div>
      <!-- *:model绑定的是script的formData -->
      <!-- *label指定的是标签自身 -->
      <el-form :label-position="'right'" label-width="60px" :model="formData">
        <el-form-item label="用户名">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="formData.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="blogLogin()" type="primary" plain>登录</el-button>
          <el-button @click="toRegister()" type="success" plain>注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    toRegister() {
      this.$router.push({ path: "/register" });
    },
    blogLogin() {
      //验证登录账号
      if (
        this.formData.username.length == 0 ||
        this.formData.password.length == 0
      ) {
        alert("表单填写完整");
        return;
      }
      //组件通过dispatch来执行action
      this.$store.dispatch("blogLogin", this.formData);
    },
  },
};
</script>

<style>
#login-page {
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* 登录框上下左右留白 */
.loginbox {
  padding: 10px 10px;
}
</style>
