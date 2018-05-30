function generatePromise(x) {
  return new Promise(resolve => resolve(x))
}

async function awaitPromise () {
  let msg = await generatePromise("messaaage")
  console.log(msg)
}

awaitPromise()
