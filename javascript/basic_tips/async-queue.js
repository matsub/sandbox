class AsyncQueue {
  constructor () {
    this._queue = []
    this._ignition = () => {}
  }

  ignite () {
    this._ignition()
    this._ignition = () => {}
  }

  enqueue (item) {
    this._queue.push(item)
    this.ignite()
  }

  async dequeue () {
    if (this._queue.length > 0) {
      return this._queue.shift()
    } else {
      return await new Promise(resolve => {
        this._ignition = () => resolve(this._queue.shift())
      })
    }
  }
}

var aq = new AsyncQueue()
async function consume (resolve) {
  while (true) {
    resolve(await aq.dequeue())
  }
}

for (let i=0; i<5; i++) aq.enqueue(i)
consume(console.log)
