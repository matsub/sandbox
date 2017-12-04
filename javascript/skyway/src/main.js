import Vue from 'vue'
import Peer from 'skyway-js'

const peer = new Peer({key: process.env.SKYWAY_KEY, debug: 3})

const app = new Vue({
  el: '#app',
  template: '<span>heyo</span>',
})
