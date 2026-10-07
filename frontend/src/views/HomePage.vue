<!-- eslint-disable-next-line vue/multi-word-component-names -->  
<template>
    <div>
    <head-bar></head-bar>
    <router-view></router-view>
    <foot-bar></foot-bar>
    </div>
</template>
<script>
import HeadBar from "../components/HeadBar.vue";
import FootBar from "../components/FootBar.vue";
// import FrontPage from "../components/FrontPage.vue";
export default {
  name: "HomePage",
  data() {
    return {};
  },
  components: {
    HeadBar,
    FootBar,
    // FrontPage,
  },
};
</script>