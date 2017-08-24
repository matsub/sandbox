class Audio {
  constructor() {
    this.context = new AudioContext()
    this._modules = []
  }

  install(module) {
    if (this.source === undefined) {
      this._modules.push(module)
    } else {
      this.source.connect(module.node)
    }
  }

  play(url) {
    loadSource(this.context, url)
      .then(source => {
        for (let module of this._modules) {
          source.connect(module.node)
        }
        source.start(0)
        this.source = source
      })
  }
}

// load the specified sound
async function loadSource(audioCtx, url) {
  var response = await fetch(url)
  var buffer = await response.arrayBuffer()

  var decoded = await audioCtx.decodeAudioData(buffer)
  var source = audioCtx.createBufferSource()
  source.buffer = decoded

  return source
}


class Volume {
  constructor(audioCtx, volume) {
    var gainNode = audioCtx.createGain()
    gainNode.gain.value = volume
    gainNode.connect(audioCtx.destination)

    this.gainNode = gainNode
  }

  set value(v) {
    this.gainNode.gain.value = v
  }

  get node() {
    return this.gainNode
  }
}
