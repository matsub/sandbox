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

  var indicator = new Indicator(audioCtx, canvas)
  var source = await loadSource(audioCtx, url)

  source.connect(indicator.node)

  var gainNode = audioCtx.createGain()
  gainNode.gain.value = 0.1

  source.connect(gainNode)
  gainNode.connect(audioCtx.destination)

  source.start(0)
}

playSoundWithIndicator("sample.ogg")
