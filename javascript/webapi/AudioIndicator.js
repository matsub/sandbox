class Indicator {
  constructor(audioCtx, canvas) {
    this.width = canvas.width
    this.height = canvas.height

    var ctx = canvas.getContext("2d")
    var gradient = ctx.createLinearGradient(0, 0, this.width, 0)

    gradient.addColorStop(0,'#004400')
    gradient.addColorStop(1,'#00ff00')
    ctx.fillStyle = gradient
    ctx.lineWidth = 4
    ctx.strokeStyle = "#ffffff"

    this.ctx = ctx
    this.audioCtx = audioCtx
  }

  draw(strength) {
    var ctx = this.ctx
    ctx.clearRect(0, 0, this.width, this.height)
    ctx.fillRect(0, 0, strength, this.height)

    for (let x=0; x < 120; x+=8) {
      ctx.beginPath()
      ctx.moveTo(x, 0)
      ctx.lineTo(x, 20)
      ctx.stroke()
    }
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

  get node() {
    // setup a analyser
    var analyser = this.audioCtx.createAnalyser()
    analyser.smoothingTimeConstant = 0.3
    analyser.fftSize = 1024

    // setup a script node
    var processor = this.audioCtx.createScriptProcessor(2048, 1, 1)
    processor.onaudioprocess = this.setup(analyser)

    analyser.connect(processor)
    processor.connect(this.audioCtx.destination)
    return analyser
  }
}


function getAverageVolume(array) {
  var sum = array.reduce((a,b)=>a+b, 0)
  return sum / array.length
}
