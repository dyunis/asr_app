let context = new AudioContext({sampleRate: 16000})

console.log('audio starting')

let sample_rate = 16000
let seconds = 10
let samples = seconds * sample_rate

let input = null
let microphone_stream = null

// prompt for mic permissions happens at navigator.getUserMedia
if (!navigator.getUserMedia) {
  navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia
}

if (navigator.getUserMedia) {
  navigator.getUserMedia({audio: true, video: false},
    function (stream) {
      start_mic(stream)
    },
    function (e) {
      alert('error with audio capture')
    }
  )
} else {
  alert('getUserMedia not support in this browser')
}
