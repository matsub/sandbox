function gp(x) {
  return new Promise(resolve => {
    resolve(x)
  })
}

async function af () {
  console.log(await gp(10))
}

af()
