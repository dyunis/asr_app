function setupAudio () {
  navigator.mediaDevices.getUserMedia({audio: true, video: false})
    .then(startMic)
    .catch(audioError)
}

function startMic (stream) {
  let context = new AudioContext({sampleRate: 16000})
}

function audioError (error) {
  alert('Audio capture error: ', error.code)
}
