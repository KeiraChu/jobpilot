import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    activeIndex: '1',
    id: null,
    positionArray: [],
    flag: false,
  },
  getters: {
    selectedPosition: (state) => (id) => {
      return state.positionArray.find(position => position.id === id);
    }
  },
  mutations: {
    updatePositionId(state, value) {
      state.positionId = value
    },
    setPositionArray(state, payload) {
      state.positionArray = payload;
    },
    setActiveIndex(state, index) {
      state.activeIndex = index;
    },
    setFlagToTrue(state) {
      state.flag = true;
    },
  },
  actions: {
    setActiveMenuItem({ commit }, index) {
      commit('setActiveIndex', index);
    }
  },
  modules: {
  }
})
