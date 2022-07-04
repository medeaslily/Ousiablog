import store from "@/store";
import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next();
      } else {
        next("/login");
      }
    },
  },
  //发布文章
  {
    path: "/add-article",
    name: "AddArticle",
    component: () => import("../views/AddArticle.vue"),
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next();
      } else {
        next("/login");
      }
    },
  },
  //文章列表
  {
    path: "/article-list",
    name: "ArticleList",
    component: () => import("../views/ArticleList.vue"),
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next();
      } else {
        next("/login");
      }
    },
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/OusiaLogin.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../views/OusiaRegister.vue"),
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

// 解决”Element-ui“与”Vuecli“这两个框架不协调发生的报错
const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch((err) => err);
};

const router = new VueRouter({
  routes,
});

export default router;
