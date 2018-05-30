const url = "https://script.google.com/macros/s/AKfycbylYt_CJN0OxcsaeTDnhFT-XIrxMiVdHSVBuCZOk_rRVSQrT7bU/exec"

// The generators also can be asynchronous...
async function* asyncGenerator (n) {
  for (let i=0; i<n; i++) {
    let response = await fetch(url)
    yield response.json()
  }
}

// check that you need to use `for await` statement to yank aync-generator
async function useAsyncGenerator () {
  for await (let item of asyncGenerator(3)) {
    console.log(item)
  }
}

useAsyncGenerator()
