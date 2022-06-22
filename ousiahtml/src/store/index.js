import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userinfo: {},
  },
  getters: {},
  mutations: {
    //保存注册登录的用户信息
    saveUserinfo(state, userinfo) {
      state.userinfo = userinfo;
    },
  },
  actions: {},
  modules: {},
});
