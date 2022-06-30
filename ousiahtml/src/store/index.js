import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import Qs from "qs";
import router from "../router";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    //定义用来保存token的状态userinfo
    userinfo: {},
  },
  getters: {
    //查询登录状态
    isnotUserlogin(state) {
      return state.userinfo.token;
    },
  },
  mutations: {
    //定义用来修改userinfo（用户信息token）的方法saveUserinfo
    saveUserinfo(state, userinfo) {
      state.userinfo = userinfo;
    },
    //清空用户数据,用来实现登出功能
    clearUserinfo(state) {
      state.userinfo = {};
    },
  },
  actions: {
    //action函数通过commit来修改mutations
    //*登录
    blogLogin({ commit }, formData) {
      //*向后端执行axios请求发送登录数据
      axios({
        url: "http://127.0.0.1:9000/api/ousia-login/",
        method: "post",
        // *Qs.stringify用来应对MultiValueDictKeyError问题
        data: Qs.stringify(formData),
      }).then((res) => {
        //*依据返回判断登录是否成功
        if (res.data == "none") {
          alert("用户名不存在");
          return;
        }
        if (res.data == "pwderr") {
          alert("密码错误");
          return;
        }
        console.log(res.data);
        //*登录成功则提交载荷保存后端返回的token到vuex
        commit("saveUserinfo", res.data);
        //添加保存token到缓存的操作， 解决一刷新页面token清空，就需要重新登录的问题
        localStorage.setItem("token", res.data.token);
        //登录成功就直接跳转到首页
        router.push({ path: "/" });
      });
    },
    //自动登录
    //在actions里定义自动登录函数（大概是为了统一管理这类函数）
    tryAutoLogin({ commit }) {
      let token = localStorage.getItem("token");
      if (token) {
        axios({
          url: "http://127.0.0.1:9000/api/auto-login/",
          method: "post",
          data: Qs.stringify({ token }),
        }).then((res) => {
          console.log(res.data);
          //依据后端返回的res.data判断是否继续执行登录成功的逻辑
          if (res.data == "tokenTimeout") {
            alert("用户信息过期，重新登陆！");
            return;
          }
          commit("saveUserinfo", res.data);
          //缓存token
          localStorage.setItem("token", res.data.token);
          //登录成功就直接跳转到首页
          router.push({ path: "/" });
        });
      }
    },
    //*注册
    blogRegister({ commit }, formData) {
      //*向后端执行axios请求发送注册数据
      axios({
        url: "http://127.0.0.1:9000/api/ousia-register/",
        method: "post",
        // *Qs.stringify用来应对MultiValueDictKeyError问题
        data: Qs.stringify(formData),
      }).then((res) => {
        console.log(res.data);
        //*依据返回判断登录是否成功
        if (res.data == "repeat") {
          alert("账号已被注册");
          return;
        }
        //*注册成功则提交载荷保存后端返回的token到vuex
        commit("saveUserinfo", res.data);
        //缓存token
        localStorage.setItem("token", res.data.token);
        router.push({ path: "/" });
      });
    },
    //登出
    //登出的功能不涉及异步操作，因此可以不在actions提交mutation
    //但为了统一管理全局变量函数，把登出与登录，注册写在一起
    blogLogout({ commit }, token) {
      commit("clearUserinfo");
      //删除缓存里的token.刷新页面将不再自动登录
      localStorage.removeItem("token");
      //不使用路由跳转来登出
      //router.push({ path: "/" });
      axios({
        url: "http://127.0.0.1:9000/api/ousia-logout/",
        method: "post",
        data: Qs.stringify({ token }),
      }).then((res) => {
        console.log(res.data);
      });
    },
  },

  modules: {},
});
