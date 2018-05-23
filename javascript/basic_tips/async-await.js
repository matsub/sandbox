async function get_ip() {
  var response = await fetch('http://ip.jsontest.com/')
  var data = response.json()
  return data
}

class C {
  constructor(val) {
    this.val = val
  }

  async fetch() {
    var ip = await get_ip()
    console.log(this.val)
    return ip.ip
  }
}

async function f() {
  var ip = await get_ip()
  console.log(ip)

  c = new C(10)
  ip = await c.fetch()
  console.log(ip)
}

f()
