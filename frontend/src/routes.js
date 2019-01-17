/* eslint-disable */
const NotFound = resolve => require(['./views/common/404.vue'], resolve);
const Home = resolve => require(['./views/Home.vue'], resolve);
const blackList = resolve => require(['./views/blackList.vue'], resolve);
const FeedView = resolve => require(['./views/FeedView.vue'], resolve);
const Links = resolve => require(['./views/ResourceLink.vue'], resolve);
const About = resolve => require(['./views/about.vue'], resolve);

let routes = [
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true,
        projectHidden: true
    },
    {
        path: '/',
        component: Home,
        name: '',
        projectHidden: true,
        children: [
            // { path: '/blackList', component: blackList, iconCls:'el-icon-bell', name: '先人指路'},
            { path: '/FeedView', component: FeedView, iconCls:'el-icon-message', name: '金玉良言'},
            { path: '/Resource', component: Links, iconCls:'el-icon-share', name: '无私奉献'},
            { path: '/About', component: About, iconCls:'el-icon-info', name: '关于我们'},
            // { path: '/robot', component: robot, iconCls:'fa fa-id-card-o', name: '消息机器人', meta: { keepAlive: false }},
            ]
    },
];

export default routes;
