let mediaRecorder

function setupAudio () {
  let constraints = {audio: {channelCount: 1, sampleRate: 16000}}
  navigator.mediaDevices.getUserMedia(constraints)
    .then(startMic)
    .catch(audioError)
}

// TODO:
// get max 15 seconds of data (unclear)
// save blob to a wav file to use as input in backend
// show backend result
//
// example at https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API

function startMic (stream) {
  mediaRecorder = new MediaRecorder(stream, {'type': 'audio/wav'})
  mediaRecorder.start(15000) // 15000ms = 15s
  console.log('starting media recorder')

  let chunks = [];
  mediaRecorder.ondataavailable = function (e) {
    console.log('data available')
    chunks.push(e.data)
    mediaRecorder.stop()
  }

  mediaRecorder.onstop = function(e) {
    console.log('stopping recorder')
    const blob = new Blob(chunks, {'type': 'audio/wav'})
    chunks = [];
    const audioURL = window.URL.createObjectURL(blob)
    // stop the stream at the end (revoke permissions)
    stream.getAudioTracks()[0].stop()
    
    const audio = document.getElementById('audio')
    const deleteButton = document.createElement('button')

    audio.setAttribute('controls', '')
    audio.src = audioURL
    deleteButton.innerHTML = 'Delete'

    let parentNode = document.getElementById('content')
    parentNode.appendChild(deleteButton)

    deleteButton.onclick = function (e) {
      let target = e.target
      audio.src = null
      audio.removeAttribute('controls')
      target.parentNode.removeChild(target)
    }
  }

}

function audioError (error) {
  alert('Audio capture error, reload the page if you already denied permissions: ', error.code)
}

function previewAudio() {
  let audio = document.getElementById('audio')
  let file = document.querySelector('input[type=file]').files[0]
  let reader = new FileReader()

  reader.onload = function () {
    audio.setAttribute('controls', '')
    audio.src = reader.result
  }

  if (file) reader.readAsDataURL(file)
}
