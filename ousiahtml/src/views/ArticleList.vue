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
          <div class="card dweb">
            <el-row>
              <!-- lg：≥1200px 响应式栅格数或者栅格属性对象 （电脑）-->
              <!-- xs：<768px 响应式栅格数或者栅格属性对象 （手机）-->
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>【小樽潮風高校Project】小春六花*小樽コラボ</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button type="danger" icon="el-icon-delete" circle></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="24">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <!-- screenWidth：由父组件App.vue在router-view标签向子组件传递的屏幕宽度 -->
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>【小樽潮風高校Project】小春六花*小樽コラボ</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button type="danger" icon="el-icon-delete" circle></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="24">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>【小樽潮風高校Project】小春六花*小樽コラボ</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button type="danger" icon="el-icon-delete" circle></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="24">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>【小樽潮風高校Project】小春六花*小樽コラボ</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button type="danger" icon="el-icon-delete" circle></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <el-col :span="24">
          <div class="card dweb">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth>500"
                  style="width: 150px; height: 100px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%; height: 200px"
                  :src="'https://otaru.jp/_sys/wp-content/uploads/2021/10/9185e1367f464541162b3bd3b54d8aa1-1-scaled.jpg'"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span>【小樽潮風高校Project】小春六花*小樽コラボ</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span>发布者:admin</span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <el-button type="success" icon="el-icon-search" circle></el-button>
                <el-button type="danger" icon="el-icon-delete" circle></el-button>
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
export default {
  props: ["screenWidth"],
  data() {
    return {
      total: 100,
      pageSize: 5,
    };
  },
  methods: {
    currentChange(cur) {
      console.log("第" + cur + "页");
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