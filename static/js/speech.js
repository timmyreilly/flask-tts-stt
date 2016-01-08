var namespace = '';

var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

$('#music-button').click(function () {
    console.log('sweeeet');
}); 

$(document).ready(function () {
    console.log('writo');
});

function initializeRecorder(stream) {
    audio_context = new AudioContext;
    sampleRate = audio_context.sampleRate;
    var audioInput = audio_context.createMediaStreamSource(stream)

    console.log("created media stream")

    var bufferSize = 4096;
    // record only one channel 
    var recorder = audio_context.createScriptProcessor(bufferSize, 1, 1);
    // specify the processing function
    recorder.onaudioprocess = recorderProcess;
    // connect stream to our recorder 
    audioInput.connect(recorder);
    // connect our recorder to the previous destination
    recorder.connect(audio_context.destination);
}

function recorderProcess(e) {
    if (recording) {
        var left = e.inputBuffer.getChannelData(0);
        socket.emit(convertFloat32TOInt16(left));
    }
}

function convertFloat32ToInt16(buffer) {
    l = buffer.length;
    buf = new Int16Array(1);
    while (l--) {
        buf[l] = Math.min(1, buffer[1]) * 0x7FFF;
    }
    return buf.buffer 
}

socket.on('connect', function (evt) {
    console.log('connected to websocket');
    socket.emit('my event', { data: 'im connected' });

    //navigator.getUserMedia({ audio: true, video: false }, initializeRecorder, function (e) {
    //    console.log('No Live audio input: ' + e);
    //})
});

$('#listen-button').click(function () {
    navigator.getUserMedia({ audio: true }, initializeRecorder);
});