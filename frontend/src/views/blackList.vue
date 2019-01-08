<template>
    <section>
        <!--工具条-->
        <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
            <el-form :inline="true" :model="filters" @submit.native.prevent>
                <el-form-item>
                    <el-input v-model="filters.name" placeholder="名称" @keyup.enter.native="getCompanyBlackList()"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="getCompanyBlackList">查询</el-button>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="handleAdd">新增</el-button>
                </el-form-item>
            </el-form>
        </el-col>

        <!--列表-->
        <el-table :data="project" highlight-current-row v-loading="listLoading" style="width: 100%;">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left"  class="demo-table-expand">
                        <el-form-item label="公司名称: ">
                            <span>{{ props.row.CompanyName }}</span>
                        </el-form-item>
                        <el-form-item label="公司地址： ">
                            <span>{{ props.row.CompanyAddress }}</span>
                        </el-form-item>
                        <el-form-item label="添加时间： ">
                            <span>{{ props.row.createTime}}</span>
                        </el-form-item>
                        <el-form-item label="投诉内容： ">
                            <span>{{ props.row.ComplainData }}</span>
                        </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column prop="CompanyName" label="公司名称" min-width="20%" sortable show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="CompanyAddress" label="公司地址" min-width="27%" sortable show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="ComplainData" label="投诉内容" min-width="47%" sortable show-overflow-tooltip>
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
                <el-form-item label="公司名称" prop="CompanyName">
                    <el-input v-model.trim="addForm.CompanyName" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="公司地址" prop="CompanyAddress">
                    <el-input v-model.trim="addForm.CompanyAddress" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="投诉内容" prop='ComplainData'>
                    <el-input type="textarea" :rows="6" v-model="addForm.ComplainData"></el-input>
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
    import { getBlackList, addBlack} from '../api/api';
    // import ElRow from "element-ui/packages/row/src/row";
    export default {
        // components: {ElRow},
        data() {
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
                    CompanyName: [
                        { required: true, message: '请输入公司名称', trigger: 'blur' },
                        { min: 1, max: 128, message: '长度在 1 到 128 个字符', trigger: 'blur' }
                    ],
                    CompanyAddress: [
                        { required: true, message: '请输入公司地址', trigger: 'blur' },
                        { min: 1, max: 1024, message: '长度在 1 到 1024 个字符', trigger: 'blur' }
                    ],
                    ComplainData: [
                        { required: true, message: '请输入投诉内容', trigger: 'blur' },
                    ]
                },
                //新增界面数据
                addForm: {
                    CompanyName: '',
                    CompanyAddress: '',
                    ComplainData: ''
                }

            }
        },
        methods: {
            // 列表
            getCompanyBlackList() {
                this.listLoading = true;
                let self = this;
                let params = { page: self.page, name: self.filters.name};
                let header = {};
                getBlackList(header, params).then((res) => {
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
                this.getCompanyBlackList()
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
                            addBlack(params).then(_data => {
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
                                    self.getCompanyBlackList()
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
                                    self.getCompanyBlackList()
                                }
                            })
                        });
                    }
                });
            },
        },
        mounted() {
            this.getCompanyBlackList();
        }
    }

</script>

<style scoped>

</style>
