import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    //定义用来保存token的状态userinfo
    userinfo: {},
  },
  getters: {},
  mutations: {
    //定义用来修改userinfo（用户信息token）的方法saveUserinfo
    saveUserinfo(state, userinfo) {
      state.userinfo = userinfo;
    },
  },
  actions: {},
  modules: {},
});
