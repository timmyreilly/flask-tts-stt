var namespace = '';

var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);


function initializeRecorder(stream) {

    console.log("initializing");
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

function convertFloat32ToInt16(buffer) {
    l = buffer.length;
    buf = new Int16Array(1);
    while (l--) {
        buf[l] = Math.min(1, buffer[1]) * 0x7FFF;
    }
    return buf.buffer
}

function recorderProcess(e) {
    if (true) {
        var left = e.inputBuffer.getChannelData(0);
        console.log(left);
        console.log(convertFloat32ToInt16(left));
        socket.emit('stream', convertFloat32ToInt16(left));
        socket.send(convertFloat32ToInt16(left));
    }
}


$('#music-button').click(function () {
    var clientMessage = "I'm the client trying to communicate";

    console.log("clicked music button");
    socket.emit("channel", clientMessage);
});

function myFunction() {
    console.log("you clicked the button");
}

function doStuff() {
    console.log("do stuff");
    navigator.getUserMedia({ audio: true, video: false }, initializeRecorder, 
        function(e){
            console.log("no live audio input" + e);
        })
}

document.getElementById("listen-button").addEventListener("click", doStuff);
