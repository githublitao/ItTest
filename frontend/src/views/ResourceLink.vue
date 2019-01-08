<template>
  <section>
    <!--工具条-->
    <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
      <el-form :inline="true" :model="filters" @submit.native.prevent>
        <el-form-item>
          <el-input v-model="filters.name" placeholder="名称" @keyup.enter.native="getResourceList"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="getResourceList">查询</el-button>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleAdd">新增</el-button>
        </el-form-item>
      </el-form>
    </el-col>

    <!--列表-->
    <el-table :data="project" highlight-current-row v-loading="listLoading" style="width: 100%;">
      <!--<el-table-column type="expand">-->
      <!--<template slot-scope="props">-->
      <!--<el-form label-position="left"  class="demo-table-expand">-->
      <!--<el-form-item label="公司名称: ">-->
      <!--<span>{{ props.row.CompanyName }}</span>-->
      <!--</el-form-item>-->
      <!--<el-form-item label="公司地址： ">-->
      <!--<span>{{ props.row.CompanyAddress }}</span>-->
      <!--</el-form-item>-->
      <!--<el-form-item label="添加时间： ">-->
      <!--<span>{{ props.row.createTime}}</span>-->
      <!--</el-form-item>-->
      <!--<el-form-item label="投诉内容： ">-->
      <!--<span>{{ props.row.ComplainData }}</span>-->
      <!--</el-form-item>-->
      <!--</el-form>-->
      <!--</template>-->
      <!--</el-table-column>-->
      <el-table-column type="index" label="#" width="100">
      </el-table-column>
      <el-table-column prop="links" label="链接地址" min-width="37%" sortable show-overflow-tooltip>
        <template slot-scope="scope">
          <a target="_blank" :href="scope.row.links">{{scope.row.links}}</a>
        </template>
      </el-table-column>
      <el-table-column prop="password" label="密码" min-width="10%" sortable show-overflow-tooltip>
      </el-table-column>
      <el-table-column prop="remarks" label="备注" min-width="47%" sortable show-overflow-tooltip>
      </el-table-column>
      <el-table-column prop="createTime" label="添加时间" min-width="16%" sortable show-overflow-tooltip>
      </el-table-column>
    </el-table>

    <!--工具条-->
    <el-col :span="24" class="toolbar">
      <el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :page-count="total" style="float:right;">
      </el-pagination>
    </el-col>

    <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false" style="width: 75%; left: 12.5%">
      <el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
        <el-form-item label="链接地址" prop="links">
          <el-input v-model.trim="addForm.links" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model.trim="addForm.password" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop='remarks'>
          <el-input type="textarea" :rows="6" v-model="addForm.remarks"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click.native="addFormVisible = false">取消</el-button>
        <el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
      </div>
    </el-dialog>
  </section>
</template>

<script>
/* eslint-disable */
  //import NProgress from 'nprogress'
  import { getLinksList, addLinks} from '../api/api';
  // import ElRow from "element-ui/packages/row/src/row";
  export default {
    // components: {ElRow},
    data() {
      var checkUrl = (rule, value, callback) => {
        var strRegex = "^((https|http|ftp|rtsp|mms)?://)"
          + "?(([0-9a-zA-z_!~*'().&=+$%-]+: )?[0-9a-zA-z_!~*'().&=+$%-]+@)?" // ftp的user@
          + "(([0-9]{1,3}\.){3}[0-9]{1,3}" // IP形式的URL- 199.194.52.184
          + "|" // 允许IP和DOMAIN（域名）
          + "([0-9a-zA-z_!~*'()-]+\.)*" // 域名- www.
          + "([0-9a-zA-z][0-9a-zA-z-]{0,61})?[0-9a-zA-z]\." // 二级域名
          + "[a-zA-z]{2,6})" // first level domain- .com or .museum
          + "(:[0-9]{1,4})?" // 端口- :80
          + "((/?)|" // a slash isn't required if there is no file name
          + "(/[0-9a-zA-z_!~*'().;?:@&=+$,%#-]+)+/?)$";
        var re = new RegExp(strRegex);
        let result = re.test(value);
        if (result) {
          return callback();
        } else {
          callback(new Error('请输入有效的链接地址！'));
        }
      };
      return {
        filters: {
          name: ''
        },
        project: [],
        total: 0,
        page: 1,
        listLoading: false,
        sels: [],//列表选中列
        addFormVisible: false,//新增界面是否显示
        addLoading: false,
        addFormRules: {
          links: [
            { required: true, message: '请输入链接地址', trigger: 'blur' },
            { validator: checkUrl }
          ],
          password: [
            { required: false, message: '请输入密码', trigger: 'blur' },
            { max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
          ],
          remarks: [
            { required: true, message: '请输入备注内容', trigger: 'blur' },
            { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
          ]
        },
        //新增界面数据
        addForm: {
          links: '',
          password: '',
          remarks: ''
        }

      }
    },
    methods: {
      // 获取项目列表
      getResourceList() {
        this.listLoading = true;
        let self = this;
        let params = { page: self.page, name: self.filters.name};
        let header = {};
        getLinksList(header, params).then((res) => {
          self.listLoading = false;
          let { msg, code, data } = res;
          if (code === '999999') {
            self.total = data.total;
            self.project = data.data
          }
          else {
            self.$message.error({
              message: msg,
              center: true,
            })
          }
        })
      },
      handleCurrentChange(val) {
        this.page = val;
        this.getResourceList()
      },
      //显示新增界面
      handleAdd: function () {
        this.addFormVisible = true;
      },
      //新增
      addSubmit: function () {
        this.$refs.addForm.validate((valid) => {
          if (valid) {
            let self = this;
            this.$confirm('确认提交吗？', '提示', {}).then(() => {
              self.addLoading = true;
              //NProgress.start();
              let params = JSON.stringify(self.addForm);
              addLinks(params).then(_data => {
                let {msg, code, data} = _data;
                self.addLoading = false;
                if (code === '999999') {
                  self.$message({
                    message: '添加成功，待管理员审核',
                    center: true,
                    type: 'success'
                  });
                  self.$refs['addForm'].resetFields();
                  self.addFormVisible = false;
                  self.getResourceList()
                } else if (code === '999997') {
                  self.$message.error({
                    message: msg,
                    center: true,
                  })
                } else {
                  self.$message.error({
                    message: msg,
                    center: true,
                  });
                  self.$refs['addForm'].resetFields();
                  self.addFormVisible = false;
                  self.getResourceList()
                }
              })
            });
          }
        });
      },
    },
    mounted() {
      this.getResourceList();
    }
  }

</script>

<style scoped lang="scss">

</style>
