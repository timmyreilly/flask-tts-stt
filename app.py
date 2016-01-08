# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on available packages.
async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()


from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_socketio import SocketIO 
from numpy import frombuffer 

app = Flask(__name__, static_path='/static')
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

from tts import get_raw_wav

@socketio.on('stream')
def audio(stream):
    first_message = True 
    total_msg = ""
    sample_rate = 0 
    print stream
    print type(stream) 
    audio_as_int_array = stream 


@socketio.on('channel')
def channel(message):
    print "received " , message 

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST']) 
def my_form_post():
    text = request.form['text'] 
    wav = get_raw_wav(text) 
    return render_template(
        'index.html',
        title = 'New Phrase',
        wavfile = wav 
        )


@app.route('/mic')
def mic():
    return render_template(
        "audio-capture.html",
        )

if __name__ == "__main__":
    socketio.run(app) 

