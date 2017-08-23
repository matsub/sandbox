class Indicator {
  constructor(canvas, width, height) {
    this.width = canvas.width
    this.height = canvas.height

    var ctx = canvas.getContext("2d")
    var gradient = ctx.createLinearGradient(0, 0, this.width, 0)

    gradient.addColorStop(1,'#00ff00')
    gradient.addColorStop(0,'#004400')
    ctx.fillStyle = gradient
    ctx.lineWidth = 4
    ctx.strokeStyle = "#ffffff"

    this.ctx = ctx
  }

  draw(strength) {
    this.ctx.clearRect(0, 0, this.width, this.height)
    this.ctx.fillRect(0, 0, strength, this.height)

    drawStripeMask(this.ctx)
  }

  setup(analyser) {
    var array =  new Uint8Array(analyser.frequencyBinCount)

    return () => {
      // get the average for the first channel
      analyser.getByteFrequencyData(array)
      var average = getAverageVolume(array)
      this.draw(average)
    }
  }

  mount(audioCtx, source) {
    // setup a analyser
    var analyser = audioCtx.createAnalyser()
    analyser.smoothingTimeConstant = 0.3
    analyser.fftSize = 1024

    // setup a script node
    var processor = audioCtx.createScriptProcessor(2048, 1, 1)
    processor.onaudioprocess = this.setup(analyser)

    var gainNode = audioCtx.createGain()
    gainNode.gain.value = 0.1

    source.connect(gainNode)
    gainNode.connect(audioCtx.destination)

    source.connect(analyser)
    analyser.connect(processor)
    processor.connect(audioCtx.destination)
  }
}


function drawStripeMask(ctx) {
  for (let x=0; x < 120; x+=8) {
    ctx.beginPath()
    ctx.moveTo(x, 0)
    ctx.lineTo(x, 20)
    ctx.stroke()
  }
}


function getAverageVolume(array) {
  var sum = array.reduce((a,b)=>a+b, 0)
  return sum / array.length
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

async function playSoundWithIndicator(url) {
  var canvas = document.querySelector("canvas")
  var audioCtx = new AudioContext()

  var indicator = new Indicator(canvas)
  var source = await loadSource(audioCtx, url)

  indicator.mount(audioCtx, source)
  source.start(0)
}

playSoundWithIndicator("sample.ogg")
