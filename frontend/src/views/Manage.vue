<template>
    <div class="manage">
      <manage-head></manage-head>
      <router-view></router-view>
      <foot-bar></foot-bar>
    </div>
</template>

<script>

import ManageHead from '../components/ManageHead.vue';
import FootBar from '../components/FootBar.vue';
export default{
  data(){
    return{}
  },
  components: {  
    ManageHead,
    FootBar,
  }
}
</script>

<style lang="less" scoped>
@import '../assets/css/demo.css';
@import '../assets/css/tabler-flags.css';
@import '../assets/css/tabler-payments.css';
@import '../assets/css/tabler-vendors.css';
@import '../assets/css/tabler.css';
      @import url('https://rsms.me/inter/inter.css');
      :root {
      	--tblr-font-sans-serif: 'Inter Var', -apple-system, BlinkMacSystemFont, San Francisco, Segoe UI, Roboto, Helvetica Neue, sans-serif;
      }
      body {
      	font-feature-settings: "cv03", "cv04", "cv11";
      }
      * {
  scrollbar-color: rgba(var(--tblr-scrollbar-color, var(--tblr-body-color-rgb)), 0.16) transparent;
}
.manage{
    display: flex;
    flex-direction: column;
    position: relative;
    min-height: 100%;
}
h1,
.h1 {
  font-size: var(--tblr-font-size-h1);
  line-height: var(--tblr-line-height-h1);
}
h3,
.h3 {
  font-size: var(--tblr-font-size-h3);
  line-height: var(--tblr-line-height-h3);
}
.mt-8 {
  margin-top: 8rem !important;
}
.mt-1 {
  margin-top: 0.25rem !important;
}
.mt-3 {
  margin-top: 1rem !important;
}
.mt-4 {
  margin-top: 1.5rem !important;
}
.px-4 {
  padding-right: 1.5rem !important;
  padding-left: 1.5rem !important;
}
.px-6 {
  padding-right: 3rem !important;
  padding-left: 3rem !important;
}
.py-3 {
  padding-top: 1rem !important;
  padding-bottom: 1rem !important;
}
.mb-2 {
  margin-bottom: 0.5rem !important;
}
.my-6 {
  margin-top: 3rem !important;
  margin-bottom: 3rem !important;
}
.py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}
.py-6 {
  padding-top: 3rem !important;
  padding-bottom: 3rem !important;
}
.px-8 {
  padding-right: 8rem !important;
  padding-left: 8rem !important;
}
.space-x-2 {
  display: flex;
  gap: 0.5rem;
}
.space-x-4 {
  display: flex;
  gap: 1.5rem;
}
.space-y-4 {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.footer {
  border-top: var(--tblr-border-width) var(--tblr-border-style) var(--tblr-border-color);
  background-color: #ffffff;
  padding: 2rem 0;
  color: var(--tblr-secondary);
  margin-top: auto;
}
</style>