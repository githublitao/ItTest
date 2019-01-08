/* eslint-disable */
import axios from 'axios';

// export const test = 'http://127.0.0.1:8000'
export const test = 'http://47.99.132.169';
// 获取公司黑名单
export const getBlackList =  (headers, params) => {
    return axios.get(`${test}/api/company/blackList`, { params: params, headers:headers}).then(res => res.data); };
// 添加公司黑名单
export const addBlack = params => { return axios.post(`${test}/api/company/blackList`, params).then(res => res.data); };
// 获取面试反馈
export const getFeedList = (headers, params) => {
    return axios.get(`${test}/api/company/feedView`, { params: params, headers:headers}).then(res => res.data); };
// 添加面试反馈
export const addFeed = params => { return axios.post(`${test}/api/company/feedView`, params).then(res => res.data); };
// 获取资源列表
export const getLinksList = (headers, params) => {
    return axios.get(`${test}/api/resource/Links`, { params: params, headers:headers}).then(res => res.data); };
// 添加资源链接
export const addLinks = params => { return axios.post(`${test}/api/resource/Links`, params).then(res => res.data); };
// 获取项目
// export const getProject = (headers, params) => {
//     return axios.get(`${test}/api/project/project_list`, { params: params, headers:headers}).then(res => res.data); };
