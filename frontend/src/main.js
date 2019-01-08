/* eslint-disable */
// import Vue from 'vue'
import App from './App'
// import ELEMENT from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from 'vue-router'
import store from './vuex/store'
import Vuex from 'vuex'
import routes from './routes'
// import 'font-awesome/css/font-awesome.min.css'
import "babel-polyfill"

Vue.config.productionTip = false;

Vue.use(ELEMENT);
// Vue.use(MINT);
Vue.use(VueRouter);
Vue.use(Vuex);

//NProgress.configure({ showSpinner: false });

const router = new VueRouter({
  // mode: 'history',
  routes
});

router.beforeEach((to, from, next) => {
  //NProgress.start();
  if (to.path === '/') {
    console.log(to.path);
    next({ path: '/FeedView', })
  } else {
    next()
  }
});


//router.afterEach(transition => {
//NProgress.done();
//});

new Vue({
  //el: '#app',
  //template: '<App/>',
  router,
  store,
  //components: { App }
  render: h => h(App)
}).$mount('#app');

