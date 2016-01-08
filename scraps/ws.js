
namespace = ''

var ws = io.connect('http://' + document.domain + ':' + location.port + namespace);




//$(document).ready(function () {

//    var session = {
//        audio: true,
//        video: false
//    };
//    var recordRTC = null;
//    navigator.getUserMedia(session, initializeRecorder, errorCallback);

//    function initializeRecorder(stream) {
//        var audio_context = new AudioContext;
//        sampleRate = audio_context.sampleRate;
//        var audioInput = audio_context.createMediaStreamSource(stream);

//        console.log("Create media stream");


//        var bufferSize = 4096;

//        var recorder = audio_context.createScriptProcessor(bufferSize, 1, 1);

//        // specify processing function
//        recorder.onaudioprocess = recorderProcess;
//        // connect stream to our recorder
//        audioInput.connect(recorder);
//        // connect our recorder to the previous destination
//        recorder.connect(audio_context.destination);
//    }

//    var namespace = '';
//    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

//    function recorderProcess(e) {
//        var left = e.inputBuffer.getChannelData(0);
//    }

//});
