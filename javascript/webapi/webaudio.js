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
    this.ctx.lineWidth = 4
    this.ctx.strokeStyle = "#ffffff"
  }

  draw(strength) {
    this.ctx.clearRect(0, 0, this.width, this.height);
    this.ctx.fillRect(0, 0, strength, this.height);

    drawStripeMask(this.ctx)
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


// get the context from the canvas to draw on
var canvas = document.querySelector("#canvas")
var indicator = new Indicator(canvas, 120, 20)

// load the sound
var audio = getAudioNode(indicator);
loadSound(audio, "sample.ogg");

function getAudioNode(indicator) {
  var context = new AudioContext();

  // setup a analyser
  var analyser = context.createAnalyser();
  analyser.smoothingTimeConstant = 0.3;
  analyser.fftSize = 1024;
  analyser.connect(context.destination);

  // setup a script node
  var scriptNode = context.createScriptProcessor(2048, 1, 1);
  scriptNode.onaudioprocess = setupIndicator(indicator, analyser)
  scriptNode.connect(analyser);

  return {
    context,
    analyser,
  }
}


// load the specified sound
function loadSound(audio, url) {
  fetch(url)
  .then(response => response.arrayBuffer())
  .then(buffer => {
    // decode the data
    audio.context.decodeAudioData(buffer)
      .then(decoded => {
      var source = audio.context.createBufferSource();
      var gainNode = audio.context.createGain();

      // setup buffer
      source.buffer = decoded;
      source.connect(audio.context.destination);

      // setup gain
      gainNode.gain.value = -0.9
      gainNode.connect(audio.analyser);
      source.connect(gainNode);

      source.start(0);
    }, console.log);
  })
}


function setupIndicator(indicator, analyser) {
  var array =  new Uint8Array(analyser.frequencyBinCount);

  return function() {
    // get the average for the first channel
    analyser.getByteFrequencyData(array);
    var average = getAverageVolume(array);

    // draw indicator
    indicator.draw(average)
  }
}


function getAverageVolume(array) {
  var sum = array.reduce((a,b)=>a+b, 0)
  return sum / array.length;
}
