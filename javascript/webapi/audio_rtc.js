/*  Compatibility shim */
navigator.getUserMedia = (
  navigator.getUserMedia
  || navigator.webkitGetUserMedia
  || navigator.mozGetUserMedia
)


class Indicator {
  constructor(canvas, width, height) {
    var ctx = canvas.getContext("2d");
    var gradient = ctx.createLinearGradient(0, 0, width, 0);

    gradient.addColorStop(1,'#00ff00');
    gradient.addColorStop(0,'#004400');
    ctx.fillStyle = gradient;

    this.width = width
    this.height = height
    this.ctx = ctx
  }

  draw(strength) {
    this.ctx.clearRect(0, 0, this.width, this.height);
    this.ctx.fillRect(0, 0, strength, this.height);
  }
}


// get the context from the canvas to draw on
var constraints = { video:false, audio:true }

navigator.mediaDevices.getUserMedia(constraints)
  .then(stream => {
    document.querySelector('audio').src = URL.createObjectURL(stream)
    var context = new AudioContext();
    var canvas = document.querySelector("#canvas")
    var indicator = new Indicator(canvas, 120, 20)

    // setup a script node
    var scriptNode = context.createScriptProcessor(2048, 1, 1);
    scriptNode.connect(context.destination);

    // setup a analyser
    var analyser = context.createAnalyser();
    analyser.smoothingTimeConstant = 0.3;
    analyser.fftSize = 1024;

    // apply indicator
    scriptNode.onaudioprocess = setupIndicator(indicator, analyser)

    var source = context.createMediaStreamSource(stream)
    source.connect(analyser)
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
