import Vue from "vue";
import App from "./App.vue";
import ElementUI from "element-ui";
import router from "./router";
import store from "./store";
import "element-ui/lib/theme-chalk/index.css";
import "./assets/css/mystyle.css";

//配置summernote。引入summernote,Bootstrap,popper.js
import "summernote";
import "summernote/dist/summernote.css";
import "summernote/lang/summernote-zh-CN.js";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "popper.js";

Vue.use(ElementUI);
Vue.config.devtools = true;
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
