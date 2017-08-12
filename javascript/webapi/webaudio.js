var context = new AudioContext();
var audioBuffer;
var sourceNode;
var analyser;
var javascriptNode;

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
setupAudioNodes();
loadSound("fly-me-to-the-moon.ogg");

function setupAudioNodes() {
  // setup a javascript node
  javascriptNode = context.createScriptProcessor(2048, 1, 1);
  // connect to destination, else it isn't called
  javascriptNode.connect(context.destination);
  // setup a analyzer
  analyser = context.createAnalyser();
  analyser.smoothingTimeConstant = 0.3;
  analyser.fftSize = 1024;

  // create a buffer source node
  sourceNode = context.createBufferSource();
  analyser.connect(javascriptNode);

  // and connect to destination
  sourceNode.connect(context.destination);
}
// load the specified sound
function loadSound(url) {
  var request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.responseType = 'arraybuffer';
  // When loaded decode the data
  request.onload = function() {
    // decode the data
    context.decodeAudioData(request.response, function(buffer) {
      // when the audio is decoded play the sound
      playSound(buffer);
    }, onError);
  }
  request.send();
}
function playSound(buffer) {
  sourceNode.buffer = buffer;
  sourceNode.start(0);
}
// log if an error occurs
function onError(e) {
  console.log(e);
}
// when the javascript node is called
// we use information from the analyzer node
// to draw the volume
javascriptNode.onaudioprocess = function() {
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
