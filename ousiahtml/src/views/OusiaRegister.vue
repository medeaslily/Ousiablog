<template>
  <div id="register-page">
    <div class="dweb loginbox">
      <div class="header">
        新用户注册
        <!-- 分割线 -->
        <el-divider></el-divider>
      </div>
      <!-- :model绑定的是script的formData -->
      <!-- label指定的是标签自身 -->
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
          <el-button @click="blogRegister()" type="primary" plain>注册</el-button>
          <el-button @click="toLogin()" type="success" plain>已有账号</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
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
      //提交注册
      axios({
        url: "http://127.0.0.1:9000/api/ousia-register/",
        method: "post",
        // Qs.stringify用来应对MultiValueDictKeyError问题
        data: Qs.stringify(this.formData),
      }).then((res) => {
        console.log(res.data);
        if (res.data == "repeat") {
          alert("账号已被注册");
          return;
        }
        this.$store.commit("saveUserinfo", res.data);
      });
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
/* 登录框上下左右留白 */
.loginbox {
  padding: 10px 10px;
}
</style>