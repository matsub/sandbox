/*  Compatibility shim */
navigator.getUserMedia = (
  navigator.getUserMedia
  || navigator.webkitGetUserMedia
  || navigator.mozGetUserMedia
)

const constraints = {
  video: {
    width: 480,
    height: 320
  },
  audio: false
}

const config = {
  iceServers: [
    { urls: 'stun:stun.l.google.com:19302' }
  ]
}

function iceNegotiation(pc) {
  return function(event) {
    pc.addIceCandidate(event.candidate)
      .catch(e => console.log('ICE gathering has finished.'))
  }
}

async function sugoi_kansuu(local, remote) {
  var pc1 = new RTCPeerConnection(config)
  var pc2 = new RTCPeerConnection(config)

  // on got ICE candidate
  pc1.onicecandidate = iceNegotiation(pc2)
  pc2.onicecandidate = iceNegotiation(pc1)

  // on got Stream
  // pc2.ontrack = e => { video.srcObject = e.stream }
  pc2.onaddstream = e => {
    remote.srcObject = e.stream
  }

  // add tracks
  var stream = await navigator.mediaDevices.getUserMedia(constraints)
  local.srcObject = stream

  pc1.addStream(stream)
  /*
  for (let track of stream.getTracks()) {
    pc1.addTrack(track, stream)
  }
  */

  /* SDP */
  // creating offer
  var offer = await pc1.createOffer()
  pc1.setLocalDescription(offer)
  pc2.setRemoteDescription(offer)

  // answering offer
  var answer = await pc2.createAnswer()
  pc2.setLocalDescription(answer)
  pc1.setRemoteDescription(answer)
}
