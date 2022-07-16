<template>
  <div id="article-list">
    <div class="dweb">
      <!-- 面包屑导航 -->
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <!-- to：路由跳转对象 -->
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>活动详情</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 文章列表 -->
    <div class="dweb" style="margin-top: 10px;">
      <el-row>
        <!-- span：栅格占据的列数，最大值24 -->
        <el-col v-for="item in articleList" :key="item.id" :span="24">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <!-- screenWidth：由父组件App.vue在router-view标签向子组件传递的屏幕宽度 -->
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>{{ item.title }}</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:{{ item.nickName }}</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button
                  @click="deleteArticle(item.id)"
                  type="danger"
                  icon="el-icon-delete"
                  circle
                ></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 分页器 -->
    <!-- total：总条目数 （由js管理数据）-->
    <!-- page-size：总页数 （由js管理数据）-->
    <!-- 实际页数=total*page-size -->
    <div class="dweb" style="margin-top: 10px;">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        :page-size="pageSize"
        @current-change="currentChange"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  props: ["screenWidth"],
  data() {
    return {
      total: 100,
      pageSize: 5,
      currentPage: 1,
      articleList: [],
    };
  },
  mounted() {
    this.getListData(this.currentChange);
  },
  methods: {
    currentChange(cur) {
      this.currentPage = cur;
      this.getListData(cur);
    },
    getListData(page) {
      axios({
        url: "http://127.0.0.1:9000/api/artitle-list/",
        method: "get",
        params: {
          page,
          pageSize: this.pageSize,
        },
      }).then((res) => {
        this.articleList = res.data.data;
        this.total = res.data.total;
      });
    },
    deleteArticle(id) {
      axios({
        url: "http://127.0.0.1:9000/api/delete-article/",
        method: "delete",
        data: Qs.stringify({
          id,
          token: this.$store.getters.isnotUserlogin,
        }),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }).then((res) => {
        if (res.data == "nologin") {
          alert("用户信息错误");
          return;
        }
        this.getListData(this.currentPage);
      });
    },
  },
};
</script>

<style>
#article-list .dweb {
  padding: 10px 10px;
}
.card.dweb .text-item {
  text-align: center;
  display: flex;
  justify-content: center;
}
</style>