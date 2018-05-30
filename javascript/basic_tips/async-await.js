// an async function can be awaited in an async function
async function ping() {
  let response = await fetch('https://script.google.com/macros/s/AKfycbylYt_CJN0OxcsaeTDnhFT-XIrxMiVdHSVBuCZOk_rRVSQrT7bU/exec')
  return response.json()
}

class C {
  // instance method can be the asynchronous!
  async fetch() {
    return await ping()
  }
}

async function f() {
  c = new C()
  console.log(await ping())
  console.log(await c.fetch())
}

f()
