const url = "http://ip.jsontest.com/"

async function* asyncGenerator (n) {
  for (let i=0; i<n; i++) {
    let response = await fetch(url)
    let data = response.json()
    yield data
  }
}

async function useAsyncGenerator () {
  for await (let item of asyncGenerator(10)) {
    console.log(item)
  }
}

useAsyncGenerator()
