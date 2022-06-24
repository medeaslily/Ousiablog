<template>
  <div id="register-page">
    <div class="dweb loginbox">
      <div class="header">
        <!-- 标题 -->
        新用户注册
        <!-- 分割线 -->
        <el-divider></el-divider>
      </div>
      <!-- 表单 -->
      <!-- *:model绑定的是script的formData -->
      <!-- *label指定的是标签自身 -->
      <el-form :label-position="'right'" label-width="70px" :model="formData">
        <el-form-item label="用户名">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="formData.password"></el-input>
        </el-form-item>
        <el-form-item label="重复密码">
          <el-input v-model="formData.password2"></el-input>
        </el-form-item>
        <el-form-item>
          <!-- 按钮 -->
          <el-button @click="blogRegister()" type="primary" plain>注册</el-button>
          <el-button @click="toLogin()" type="success" plain>已有账号</el-button>
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
        password2: "",
      },
    };
  },
  methods: {
    blogRegister() {
      // 验证注册账号
      if (
        this.formData.username.length == 0 ||
        this.formData.password.length == 0 ||
        this.formData.password2.length == 0
      ) {
        alert("表单尚未填写完整");
        return;
      }
      if (this.formData.password.length < 8) {
        alert("密码长度不能小于8");
        return;
      }
      if (this.formData.password != this.formData.password2) {
        alert("密码不一致");
        return;
      }
      //组件通过dispatch来执行action
      this.$store.dispatch("blogRegister", this.formData);
    },
    toLogin() {
      this.$router.push({ path: "/login" });
    },
  },
};
</script>

<style>
#register-page {
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* *登录框上下左右留白 */
.loginbox {
  padding: 10px 10px;
}
</style>