const vis = require("vis")

var nodes = new vis.DataSet([
  {id: 1, label: "A"},
  {id: 2, label: "B"},
  {id: 3, label: "C"},
  {id: 4, label: "D"},
  {id: 5, label: "E"}
])
var edges = new vis.DataSet([
  {from: 1, to: 3},
  {from: 1, to: 2},
  {from: 2, to: 4},
  {from: 2, to: 5}
])

var container = document.getElementById('mynetwork')
var data = { nodes, edges }
var options = {
  manipulation: {
    addEdge: (edge, callback) => callback(edge)
  }
}
var network = new vis.Network(container, data, options)

document.getElementById('add').onclick = evt => nodes.add({id: 6, label: "new"})
document.getElementById('connect').onclick = evt => edges.add({from: 3, to: 4})
