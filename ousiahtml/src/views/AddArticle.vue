<template>
  <div id="add-article">
    <el-row :gutter="10">
      <el-col :xs="24" :lg="8">
        <div class="dweb">
          <el-form :label-position="'left'" label-width="80px" :model="article_info">
            <el-form-item label="文章标题">
              <el-input v-model="article_info.title"></el-input>
            </el-form-item>
            <el-form-item label="描述">
              <el-input rows="4" type="textarea" v-model="article_info.describe"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
      <el-col :xs="24" :lg="16">
        <div class="dweb">
          <div v-for="(img,index) in cover_list" :key="index">
            <el-image
              当用户鼠标点击预览图片保持住hover的样式
              v-if="img==cover_img"
              class="cover"
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
            <el-image
              v-else
              class
              style="width: 150px; height: 150px"
              :src="img"
              :fit="'cover'"
              @click="chooseCover(img)"
            ></el-image>
          </div>
          <el-button @click="submitArticle" type="success" round>保存文章</el-button>
        </div>
      </el-col>
      <el-col :xs="24" :lg="24">
        <div class="dweb">
          <div id="summernote"></div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";
import QS from "qs";
export default {
  data() {
    return {
      article_info: {
        title: "",
        describe: "",
        contents: "",
      },
      //选中的封面
      cover_img: "",
      //提供给预览使用的图片列表
      cover_list: [],
    };
  },
  mounted() {
    this.summernote();
  },
  methods: {
    //保存文章
    submitArticle() {
      let article_data = {
        title: this.article_info.title,
        describe: this.article_info.describe,
        content: this.article_info.contents,
        cover: this.cover_img,
        token: this.$store.getters.isnotUserlogin,
      };
      axios
        .post(
          "http://127.0.0.1:9000/api/add-article/",
          QS.stringify(article_data)
        )
        .then((res) => {
          console.log(res);
          if (res.data == "notitle") {
            alert("标题为空");
            return;
          }
          if (res.data == "nologin") {
            alert("用户信息错误");
            return;
          }
          if (res.data == "ok") {
            window.location.reload();
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 配置summernote的$来自jquery
    summernote() {
      //提前存入this，否者this会改变
      let self = this;
      $("#summernote").summernote({
        width: "100%",
        height: 500,
        lang: "zh-CN",
        // 回调函数
        callbacks: {
          //当输入,contents为框架规范
          onChange(contents) {
            self.article_info.contents = contents;
          },

          //图片上传回调函数
          onImageUpload(files) {
            //console.log(files);
            //使用浏览器提供的readAsDataURL方法把files转换为携带图片二进制信息的imgData
            let img = files[0];
            let imgData = new FileReader();
            imgData.readAsDataURL(img);
            //console.log(imgData);
            //进一步找到imgData里的图片二进制信息
            imgData.onload = function () {
              //console.log(imgData.result);

              //插入图片到富文本框内
              //JS的一个结点可以等于html的img标签来用
              let imgnode = document.createElement("img");
              imgnode.src = imgData.result;
              //把结点插入到summernote里
              $("#summernote").summernote("insertNode", imgnode);

              //把图片二进制信息imgData.result储存到cover_list，推入封面待选择
              self.cover_list.push(imgData.result);
            };
          },

          // 远程图片上传回调函数
          onImageLinkInsert(url) {
            //console.log(url);
            // 生成一个img结点
            let imgnode = document.createElement("img");
            // 绑定结点的src属性
            imgnode.src = url;
            //console.log(imgnode);
            //把结点插入到summernote里，使其在富文本框里展示
            $("#summernote").summernote("insertNode", imgnode);
            //只需推入图片的url给cover_list给el-image，使其在预览展示
            self.cover_list.push(url);
          },

          //媒体删除回调函数
          onMediaDelete(target) {
            let imgData = target[0].src;
            console.log(imgData);
            for (let i = 0; i < self.cover_list.length; i++) {
              //splice(index, count)
              if (self.cover_list[i] == imgData) self.cover_list.splice(i, 1);
            }
          },
        },
      });
    },
    //选择封面
    chooseCover(img) {
      this.cover_img = img;
    },
  },
};
</script>

<style scoped>
.dweb {
  min-height: 200px;
  padding: 20px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* el-form-item的下边距使得它无法垂直居中 */
.el-form-item {
  margin-top: 22px;
}
/* 保存文章 */
.dweb .el-button {
  position: fixed;
  right: 20px;
  margin-top: 250px;
  z-index: 1001;
}
/* 预览图片 */
.dweb .el-image:hover {
  border: 2px solid rgb(255, 2, 2);
}
.dweb .el-image.cover {
  border: 2px solid rgb(255, 2, 2);
}
</style>