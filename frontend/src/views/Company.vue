<template>
    <div class="com">
        <com-head></com-head>
        <router-view></router-view>
        <foot-bar></foot-bar>
    </div>
</template>
<script>
import FootBar from "../components/FootBar.vue";
import ComHead from "../components/ComHead.vue";
export default {
    data() {
    return {};
  },
  components: {
    FootBar,
    ComHead,
  },
};
</script>
