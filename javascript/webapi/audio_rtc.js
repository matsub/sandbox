/*  Compatibility shim */
navigator.getUserMedia = (
  navigator.getUserMedia
  || navigator.webkitGetUserMedia
  || navigator.mozGetUserMedia
)


class Indicator {
  constructor(canvas) {
    this.width = canvas.width
    this.height = canvas.height

    var ctx = canvas.getContext("2d");
    var gradient = ctx.createLinearGradient(0, 0, this.width, 0);

    gradient.addColorStop(1,'#00ff00');
    gradient.addColorStop(0,'#004400');
    ctx.fillStyle = gradient;

    this.ctx = ctx
    this.ctx.lineWidth = 4
    this.ctx.strokeStyle = "#ffffff"
  }

  draw(strength) {
    this.ctx.clearRect(0, 0, this.width, this.height);
    this.ctx.fillRect(0, 0, strength, this.height);

    for (let x=0; x < this.width; x+=8) {
      this.ctx.beginPath()
      this.ctx.moveTo(x, 0)
      this.ctx.lineTo(x, this.height)
      this.ctx.stroke()
    }
  }
}


// get the context from the canvas to draw on
var constraints = { video:false, audio:true }

navigator.mediaDevices.getUserMedia(constraints)
  .then(stream => {
    var context = new AudioContext();
    var canvas = document.querySelector("#canvas")
    var indicator = new Indicator(canvas)

    // setup a analyser
    var analyser = context.createAnalyser();
    analyser.smoothingTimeConstant = 0.3;
    analyser.fftSize = 1024;

    // setup a script node
    var scriptNode = context.createScriptProcessor(2048, 1, 1);
    scriptNode.connect(context.destination);
    scriptNode.onaudioprocess = setupIndicator(indicator, analyser)

    var source = context.createMediaStreamSource(stream)
    source.connect(analyser)
    document.querySelector('audio').src = URL.createObjectURL(stream)
  })


function setupIndicator(indicator, analyser) {
  return function() {
    var array =  new Uint8Array(analyser.frequencyBinCount);

    // get the average for the first channel
    analyser.getByteFrequencyData(array);
    var average = getAverageVolume(array);

    // draw indicator
    indicator.draw(average*2)
  }
}


function getAverageVolume(array) {
  var sum = array.reduce((a,b)=>a+b, 0)
  return sum / array.length;
}
