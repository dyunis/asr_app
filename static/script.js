function setupAudio () {
  let constraints = {audio: {channelCount: 1, sampleRate: 16000}}
  navigator.mediaDevices.getUserMedia(constraints)
    .then(startMic)
    .catch(audioError)
}

// get max 15 seconds of data
// map stream to blob with wav format
// show in window
// save blob to a wav file to use as input in backend
// show backend result

function startMic (stream) {
  const mediaRecorder = new MediaRecorder(stream)
  mediaRecorder.start(160000)
  console.log('starting media recorder')

  let chunks = []
  mediaRecorder.ondataavailable = function (e) {
    chunks.push(e.data)
    mediaRecorder.stop()
  }

  mediaRecorder.onstop = function(e) {
    const blob = new Blob(chunks, {'type': 'audio/wav'})
    chunks = []
    const audioURL = window.URL.createObjectURL(blob)
    // stop the stream at the end (revoke permissions)
    stream.getAudioTracks()[0].stop()
  }
}

function audioError (error) {
  alert('Audio capture error, reload the page if you already denied permissions: ', error.code)
}
