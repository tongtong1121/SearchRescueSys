import Vue from "vue";
import Router from "vue-router";
import CaseListContent from "./views/content/CaseListContent/CaseList.vue";
import WindMap from "./views/content/wind/windMap.vue";
import CurrentMap from "./views/content/current/currentMap.vue";
import RescueMap from "./views/content/rescue/rescueContent.vue";
import OilMap from "./views/content/oilspilling/oilSpillingMap.vue";
import OilMapNew from "./views/content/oilspilling/oilSpillingMap2.vue";
import OilMapMerge from "./views/content/oilspilling/oilSpillingMap3.vue";
// import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/caselist",
      name: "caselist",
      component: CaseListContent
    },
    {
      path: "/windmap",
      name: "windmap",
      component: WindMap
    },
    {
      path: "/currentmap",
      name: "currentmap",
      component: CurrentMap
    },
    {
      path: "/rescuemap",
      name: "rescuemap",
      component: RescueMap
    },
    {
      path: "/oilmap",
      name: "oilmap",
      component: OilMap
    },
    {
      path: "/newoilmap",
      name: "newoilmap",
      component: OilMapNew
    },
    {
      path: "/mergeoilmap",
      name: "mergeoilmap",
      component: OilMapMerge
    }
    // {
    //   path: "/about",
    //   name: "about",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "./views/About.vue")
    // }
  ]
});
