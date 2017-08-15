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
var canvas = document.querySelector("#canvas")
var indicator = new Indicator(canvas, 120, 20)

// load the sound
var audio = getAudioNode(indicator);
loadSound(audio, "sample.ogg");

function getAudioNode(indicator) {
  var context = new AudioContext();

  // setup a script node
  var scriptNode = context.createScriptProcessor(2048, 1, 1);
  scriptNode.connect(context.destination);

  // setup a analyser
  var analyser = context.createAnalyser();
  analyser.smoothingTimeConstant = 0.3;
  analyser.fftSize = 1024;
  analyser.connect(context.destination);

  // apply indicator
  scriptNode.onaudioprocess = setupIndicator(indicator, analyser)

  // create a buffer source node
  var source = context.createBufferSource();
  source.connect(analyser);

  var gainNode = context.createGain();
  source.connect(gainNode);
  gainNode.connect(context.destination);

  return {
    context,
    source,
    gainNode
  }
}


// load the specified sound
function loadSound(audio, url) {
  fetch(url)
  .then(response => response.arrayBuffer())
  .then(buffer => {
    // decode the data
    audio.context.decodeAudioData(buffer, decoded => {
      // when the audio is decoded play the sound
      audio.source.buffer = decoded;
      audio.source.start(0);
      audio.gainNode.gain.value = -0.9
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
