const vis = require("vis")

var nodes = new vis.DataSet([
  {id: 'a', label: "A"},
  {id: 'b', label: "B"},
  {id: 'c', label: "C"},
  {id: 'd', label: "D"},
  {id: 'e', label: "E"}
])
var edges = new vis.DataSet([
  {from: 'a', to: 'b'},
  {from: 'a', to: 'c'},
  {from: 'b', to: 'd'},
  {from: 'b', to: 'e'}
])

var container = document.getElementById('mynetwork')
var data = { nodes, edges }
var options = {
  manipulation: {
    addEdge: (edge, callback) => callback(edge)
  }
}
var network = new vis.Network(container, data, options)

document.getElementById('add').onclick = evt => nodes.add({id: 'f', label: "F"})
document.getElementById('connect').onclick = evt => edges.add({from: 'e', to: 'd'})
