import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueCompositionApi from "@vue/composition-api";
import Vue from "vue";

Vue.use(VueCompositionApi);

createApp(App).use(store).use(router).mount("#app");
