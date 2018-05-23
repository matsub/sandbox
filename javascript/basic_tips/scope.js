class A {
  constructor(value) {
    this.value = value
  }

  arrow_method() {
    return new Promise((resolve, reject) => {
      // このときthisはAのインスタンスを指す
      resolve(this.value)
    })
  }

  func_method() {
    return new Promise(function (resolve, reject) {
      // このときfunctionに束縛される
      resolve(this.value)
    })
  }
}

a = new A(12)
a.arrow_method().then(console.log)
// >> 12
a.func_method().then(console.log)
// TypeError: Cannot read property 'value' of undefined
