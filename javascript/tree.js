function min(objs, key) {
  let least = objs[0]
  for (let obj of objs) {
    if ( key(least, obj) ) {
      least = obj
    }
  }
  return least
}

class Tree {
  constructor(value, MAX_LENGTH=2){
    this.value = value
    this.MAX_LENGTH = MAX_LENGTH
    this.children = []
  }

  get size() {
    if (this._size === undefined) {
      let sum = this.children.length
      for (let child of this.children) {
        sum += child.size
      }
      this._size = sum
      return sum
    } else {
      return this._size
    }
  }

  addChild(value){
    if (this._size !== undefined) { this._size += 1 }
    if (this.children.length < this.MAX_LENGTH) {
      let child = new Tree(value, this.MAX_LENGTH)
      this.children.push(child)
      return this.value
    } else {
      let parentNode = min(this.children, (a, b) => {
        return a.size > b.size
      })
      return parentNode.addChild(value)
    }
  }

  removeChild(target){
    function remove(tree){
      if (tree._size !== undefined) {
        delete tree._size
      }
      for (let i in tree.children) {
        if (tree.children[i].value === target) {
          delete tree.children[i]
          tree.children.splice(i, 1)
          return
        } else {
          remove(tree.children[i])
        }
      }
    }

    remove(this)
  }
}
