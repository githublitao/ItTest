<template>
    <section>
        <!--工具条-->
        <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
            <el-form :inline="true" :model="filters" @submit.native.prevent>
                <el-form-item>
                    <el-input v-model="filters.name" placeholder="名称" @keyup.enter.native="getFeedList"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="getFeedList">查询</el-button>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="handleAdd">新增</el-button>
                </el-form-item>
            </el-form>
        </el-col>

        <!--列表-->
        <el-table :data="project" highlight-current-row stripe v-loading="listLoading" style="width: 100%;">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" class="demo-table-expand">
                        <el-col :span="12">
                            <el-form-item label="公司名称: ">
                                <span>{{ props.row.CompanyName }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="公司地址： ">
                                <span>{{ props.row.CompanyAddress }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="薪资范围： ">
                                <span>{{ props.row.SalaryRange? props.row.SalaryRange: "空"}}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="面试时间： ">
                                <span>{{ props.row.InterviewTime }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="面试岗位： ">
                                <span>{{ props.row.InterviewPost }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="面试次数： ">
                                <span>{{ props.row.InterviewNumb }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="面试时长： ">
                                <span>{{ props.row.InterviewerLong }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="是否外包： ">
                                <span>{{ props.row.outsourcing?"是":"不是" }}</span>
                            </el-form-item>
                        </el-col>
                        <el-col :span="12">
                            <el-form-item label="外包性质： ">
                                <span>{{ props.row.outsourcing? props.row.outsourcingNature: "空"}}</span>
                            </el-form-item>
                        </el-col>
                        <el-form-item label="笔试题： ">
                            <el-button type="primary" size="small" @click="handleDownload(props.row.WriteQuestion)" v-if="props.row.WriteQuestion">下载</el-button>
                            <span  v-if="!props.row.WriteQuestion">空</span>
                        </el-form-item>
                        <el-form-item label="公司福利： ">
                            <span>{{ props.row.welfare? props.row.welfare: "空"}}</span>
                        </el-form-item>
                        <el-form-item label="公司印象： ">
                            <span>{{ props.row.CompanyImage? props.row.CompanyImage: "空"}}</span>
                        </el-form-item>
                        <el-form-item label="面试官印象： ">
                            <span>{{ props.row.InterviewerImpression? props.row.InterviewerImpression: "空"}}</span>
                        </el-form-item>
                        <el-form-item label="沟通重点： ">
                            <span>{{ props.row.CommunicationKey? props.row.CommunicationKey: "空"}}</span>
                        </el-form-item>
                        <el-form-item label="总结/公司： ">
                            <span>{{ props.row.InterviewSummaryToCompany? props.row.InterviewSummaryToCompany: "空"}}</span>
                        </el-form-item>
                        <el-form-item label="总结/个人： ">
                            <span>{{ props.row.InterviewSummaryToPerson? props.row.InterviewSummaryToPerson: "空"}}</span>
                        </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column prop="CompanyName" label="公司名称" min-width="20%" sortable show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="CompanyAddress" label="公司地址" min-width="28%" sortable show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="InterviewPost" label="面试岗位" min-width="37%" sortable show-overflow-tooltip>-->
            </el-table-column>
            <el-table-column prop="createTime" label="添加时间" min-width="16%" sortable show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="面试题" min-width="10%">
                <template slot-scope="scope">
                    <el-button type="primary" size="small" @click="handleDownload(scope.row.WriteQuestion)" v-if="scope.row.WriteQuestion">下载</el-button>
                    <span  v-if="!scope.row.WriteQuestion">空</span>
                </template>
            </el-table-column>
        </el-table>

        <!--工具条-->
        <el-col :span="24" class="toolbar">
            <el-pagination layout="prev, pager, next" @current-change="handleCurrentChange" :page-size="20" :page-count="total" style="float:right;">
            </el-pagination>
        </el-col>

        <!--新增界面-->
        <el-dialog title="新增" :visible.sync="addFormVisible" :close-on-click-modal="false" style="width: 105%">
            <el-form :model="addForm" label-width="100px" :rules="addFormRules" ref="addForm" inline>
                <el-form-item label="公司名称:" prop="CompanyName">
                    <el-input v-model.trim="addForm.CompanyName" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="公司地址:" prop="CompanyAddress">
                    <el-input v-model.trim="addForm.CompanyAddress" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="薪资范围:">
                    <el-input v-model.trim="addForm.SalaryRange" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="公司福利:" prop='welfare'>
                    <el-input v-model="addForm.welfare" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="面试时间:" prop='InterviewTime'>
                    <el-date-picker v-model="addForm.InterviewTime" align="right" type="date" placeholder="选择日期" style="width: 202px;"
                                    :picker-options="pickerOptions1">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="面试岗位:" prop="InterviewPost">
                    <el-input v-model="addForm.InterviewPost" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="面试次数:" prop="InterviewNumb">
                    <el-input v-model="addForm.InterviewNumb" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="面试时长:" prop="InterviewerLong">
                    <el-input v-model="addForm.InterviewerLong" auto-complete="off"></el-input>
                </el-form-item>
                <el-form-item label="是否外包:" prop="outsourcing">
                    <el-select v-model="addForm.outsourcing" placeholder="请选择" style="width: 202px;">
                        <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="外包性质:" prop="outsourcingNature" v-if="addForm.outsourcing==='true'">
                    <el-select v-model="addForm.outsourcingNature" placeholder="请选择" style="width: 202px;">
                        <el-option label="人力外包" value="人力外包"></el-option>
                        <el-option label="项目外包" value="项目外包"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="笔试题:" prop='WriteQuestion' style="width: 100%;">
                    <el-upload
                            class="upload-demo"
                            :action="url"
                            :on-preview="handlePreview"
                            :on-remove="handleRemove"
                            multiple
                            :limit="1"
                            :on-exceed="handleExceed"
                            :on-success="handleSuccess"
                            :beforeUpload="beforeAvatarUpload"
                            :file-list="fileList">
                        <el-button size="small" type="primary">点击上传</el-button>
                        <div slot="tip" class="el-upload__tip">多文件可打包压缩，且不超过5M！</div>
                    </el-upload>
                </el-form-item>
                <el-form-item label="公司印象:" prop="CompanyImage" style="width: 100%;">
                    <el-input v-model="addForm.CompanyImage" auto-complete="off" style="width: 495px;"></el-input>
                </el-form-item>
                <el-form-item label="面试官印象:" prop='InterviewerImpression' style="width: 100%;">
                    <el-input v-model="addForm.InterviewerImpression" auto-complete="off" style="width: 495px;"></el-input>
                </el-form-item>
                <el-form-item label="沟通重点:" prop="CommunicationKey" style="width: 100%;">
                    <el-input type="textarea" :rows="3" v-model="addForm.CommunicationKey" style="width: 495px;"></el-input>
                </el-form-item>
                <el-form-item label="总结/公司:" prop="InterviewSummaryToCompany" style="width: 100%;">
                    <el-input type="textarea" :rows="3" v-model="addForm.InterviewSummaryToCompany" style="width: 495px;"></el-input>
                </el-form-item>
                <el-form-item label="总结/个人:" prop="InterviewSummaryToPerson" style="width: 100%;">
                    <el-input type="textarea" :rows="3" v-model="addForm.InterviewSummaryToPerson" style="width: 495px;"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="CloaseAdd">取消</el-button>
                <el-button type="primary" @click.native="addSubmit" :loading="addLoading">提交</el-button>
            </div>
        </el-dialog>
    </section>
</template>

<script>
/* eslint-disable */
    //import NProgress from 'nprogress'
    import { test } from '../api/api';
    import { getFeedList, addFeed} from '../api/api';
    // import moment from "moment"
    // import ElRow from "element-ui/packages/row/src/row";
    export default {
        // components: {ElRow},
        data() {
            return {
                url: test+"/api/company/updata",
                fileList: [],
                filters: {
                    name: ''
                },
                // filenumb: 1,
                options:
                    [{
                        value: "true", label: "是"
                    },
                        {
                            value: "false", label: "否"
                        }],
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
                    InterviewTime: [
                        {  type: 'date', required: true, message: '请输入面试时间', trigger: 'blur' },
                    ],
                    InterviewPost: [
                        { required: true, message: '请输入面试岗位', trigger: 'blur' },
                        { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
                    ],
                    InterviewNumb: [
                        { required: true, message: '请输入面试次数', trigger: 'blur' },
                    ],
                    InterviewerLong: [
                        { required: true, message: '请输入面试时长', trigger: 'blur' },
                        { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
                    ],
                    outsourcing: [
                        { required: true, message: '请选择是否外包', trigger: 'blur' },
                    ],
                },
                //新增界面数据
                addForm: {
                    CompanyName: '',
                    CompanyAddress: '',
                    SalaryRange: '',
                    InterviewTime: '',
                    InterviewPost: '',
                    InterviewNumb: '',
                    CompanyImage: '',
                    InterviewerImpression: '',
                    InterviewerLong: '',
                    outsourcing: '',
                    outsourcingNature: '项目外包',
                    WriteQuestion: '',
                    CommunicationKey: '',
                    InterviewSummaryToCompany: '',
                    InterviewSummaryToPerson: '',
                    welfare: '',

                },
                pickerOptions1: {
                    disabledDate(time) {
                        return time.getTime() > Date.now();
                    },
                    shortcuts: [{
                        text: '今天',
                        onClick(picker) {
                            picker.$emit('pick', new Date());
                        }
                    }, {
                        text: '昨天',
                        onClick(picker) {
                            const date = new Date();
                            date.setTime(date.getTime() - 3600 * 1000 * 24);
                            picker.$emit('pick', date);
                        }
                    }, {
                        text: '一周前',
                        onClick(picker) {
                            const date = new Date();
                            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
                            picker.$emit('pick', date);
                        }
                    }]
                }
            }
        },
        methods: {
            // 文件大小限制
            beforeAvatarUpload(file){
                const isLt2M = file.size / 1024 / 1024 < 5;
                if(!isLt2M) {
                    this.$message({
                        message: '上传文件大小不能超过 5MB!',
                        type: 'warning'
                    });
                }
                return isLt2M
            },
            handleDownload(data) {
                console.log(data);
                window.open(test+"/api/company/download?url="+data)
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            },
            handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            handleSuccess(response, file, fileList){
                this.addForm.WriteQuestion = response.data
            },
            // 获取项目列表
            getFeedList() {
                this.listLoading = true;
                let self = this;
                let params = { page: self.page, name: self.filters.name};
                let header = {};
                getFeedList(header, params).then((res) => {
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
                this.getFeedList()
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
                            console.log(typeof self.addForm["InterviewTime"])
                            let params = self.addForm;
                            params["InterviewTime"] = moment(params["InterviewTime"]).format("YYYY-MM-DD HH:mm:ss");
                            if (params["outsourcing"] === 'true'){
                                params["outsourcing"] = true
                            } else {
                                params["outsourcing"] = false
                            }
                            addFeed(params).then(_data => {
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
                                    self.getFeedList()
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
                                    self.getFeedList()
                                }
                            })
                        });
                    }
                });
            },
            CloaseAdd(){
                this.addFormVisible = false;
                this.$refs['addForm'].resetFields();
            }
        },
        mounted() {
            this.getFeedList();
        }
    }

</script>

<style scoped>

</style>
