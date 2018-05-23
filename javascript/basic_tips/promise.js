function gp(x) {
  return new Promise(resolve => {
    resolve(x)
  })
}

lsn = null

async function af () {
  console.log(await new Promise(resolve => {
    lsn = function() {
      resolve(1000)
    }
  }))
}

af()
// setTimeout(lsn, 1000)
