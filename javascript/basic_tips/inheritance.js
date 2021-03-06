class Parent {
  constructor(value) {
    this.value = value
  }

  instance_method() {
    console.log('I am parent')
    console.log(this.value)
  }
}

class Child extends Parent {
  instance_method() {
    super.instance_method()
    console.log('I am child')
    console.log(this.value)
  }
}

var child = new Child(10)
child.instance_method()
