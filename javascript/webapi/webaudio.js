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
  let context = new AudioContext();
  let source, splitter, analyser;
  let javascriptNode;

  // setup a javascript node
  javascriptNode = context.createScriptProcessor(2048, 1, 1);

  // connect to destination, else it isn't called
  javascriptNode.connect(context.destination);

  // setup a analyser
  analyser = context.createAnalyser();
  analyser.smoothingTimeConstant = 0.3;
  analyser.fftSize = 1024;

  // create a buffer source node
  source = context.createBufferSource();
  splitter = context.createChannelSplitter();

  // connect the source to the analyser and the splitter
  source.connect(splitter);

  // connect one of the outputs from the splitter to
  // the analyser
  splitter.connect(analyser,0,0);

  // connect the splitter to the javascriptnode
  // we use the javascript node to draw at a
  // specific interval.
  analyser.connect(javascriptNode);

  // setup indicator
  javascriptNode.onaudioprocess = setupIndicator(analyser)

  // and connect to destination
  source.connect(context.destination);

  return {
    context,
    source,
  }
}


// load the specified sound
function loadSound(audio, url) {
  let request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';

  // When loaded decode the data
  request.onload = function() {
    // decode the data
    audio.context.decodeAudioData(request.response, function(buffer) {
      // when the audio is decoded play the sound
      audio.source.buffer = buffer;
      audio.source.start(0);
    }, console.log);
  }

  request.send();
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

    // set the fill style
    ctx.fillStyle=gradient;

    // create the meters
    ctx.fillRect(0,130-average,25,130);
  }
}


function getAverageVolume(array) {
  var values = 0;
  var average;
  var length = array.length;
  // get all the frequency amplitudes
  for (var i = 0; i < length; i++) {
    values += array[i];
  }
  average = values / length;
  return average;
}
