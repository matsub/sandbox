// get the context from the canvas to draw on
var ctx = document.querySelector("#canvas").getContext("2d");

// create a gradient for the fill. Note the strange
// offset, since the gradient is calculated based on
// the canvas, not the specific element we draw
var gradient = ctx.createLinearGradient(0,0,0,130);
gradient.addColorStop(1,'#000000');
gradient.addColorStop(0.75,'#ff0000');
gradient.addColorStop(0.25,'#ffff00');
gradient.addColorStop(0,'#ffffff');

// load the sound
var audio = getAudioNode();
loadSound(audio, "fly-me-to-the-moon.ogg");

function getAudioNode() {
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
  scriptNode.onaudioprocess = setupIndicator(analyser)

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


// when the javascript node is called
// we use information from the analyser node
// to draw the volume
function setupIndicator(analyser) {
  return function() {
    // get the average for the first channel
    var array =  new Uint8Array(analyser.frequencyBinCount);
    analyser.getByteFrequencyData(array);
    var average = getAverageVolume(array);

    // clear the current state
    ctx.clearRect(0, 0, 60, 130);
    ctx.fillStyle=gradient;
    ctx.fillRect(0,130-average,25,130);
  }
}


function getAverageVolume(array) {
  var sum = array.reduce((a,b)=>a+b, 0)
  return sum / array.length;
}
