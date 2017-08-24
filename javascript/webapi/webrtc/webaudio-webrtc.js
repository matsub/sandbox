/*  Compatibility shim */
navigator.getUserMedia = (
  navigator.getUserMedia
  || navigator.webkitGetUserMedia
  || navigator.mozGetUserMedia
)

var constraints = {
  video:false,
  audio:true
}

async function getStreamSource(audioCtx) {
  var stream = await navigator.mediaDevices.getUserMedia(constraints)
  return audioCtx.createMediaStreamSource(stream)
}

async function createVoiceHandler(audioCtx, canvas) {
  var source = await getStreamSource(audioCtx)
  var indicator = new Indicator(audioCtx, canvas)

  var gainNode = audioCtx.createGain()
  gainNode.gain.value = 1

  source.connect(indicator.node)
  source.connect(gainNode)
  gainNode.connect(audioCtx.destination)

  return gainNode
}

class Voice {
  constructor(audioCtx, canvas) {
    createVoiceHandler(audioCtx, canvas)
      .then(gainNode => {
        this.gainNode = gainNode
      })
  }

  set volume(value) {
    this.gainNode.gain.value = value
  }
}
