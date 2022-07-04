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
        <el-col :span="24">
          <div v-for="item in article_list" :key="item.id" class="card dweb">
            <el-row>
              <!-- lg：≥1200px 响应式栅格数或者栅格属性对象 （电脑）-->
              <!-- xs：<768px 响应式栅格数或者栅格属性对象 （手机）-->
              <el-col :xs="24" :lg="6">
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
        :current-page="currentPage"
        @current-change="currentChange"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import QS from "qs";
export default {
  props: ["screenWidth"],
  data() {
    return {
      //currentPage:当前页数
      currentPage: 1,
      total: 100,
      pageSize: 5,
      article_list: [],
    };
  },
  mounted() {
    this.getListData(this.currentPage);
  },
  methods: {
    // 删除文章
    deleteArticle(id) {
      if (confirm("是否删除？")) {
        axios({
          url: "http://127.0.0.1:9000/api/delete-article/",
          method: "delete",
          data: QS.stringify({
            id,
            token: this.$store.getters.isnotUserlogin,
          }),
          // 针对后端Media Type问题的首部信息
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }).then((res) => {
          console.log(res.data);
          if (res.data == "nologin") {
            alert("用户信息过期");
            return;
          }
          this.getListData(this.currentPage);
        });
      }
    },
    getListData(page) {
      axios({
        url: "http://127.0.0.1:9000/api/artitle-list",
        method: "get",
        params: {
          page,
          pageSize: this.pageSize,
        },
      }).then((res) => {
        console.log(res.data);
        this.article_list = res.data.data;
        this.total = res.data.total;
      });
    },
    //分页器监听函数
    currentChange(cur) {
      this.currentPage = cur;
      this.getListData(cur);
    },
  },
};
</script>

<style>
#article-list .dweb {
  padding: 20px 10px;
}
.card.dweb .text-item {
  text-align: center;
  display: flex;
  justify-content: center;
}
</style>