import io
import os

from flask import Flask, request, render_template, redirect, send_from_directory
import scipy.io.wavfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 3
app.config['UPLOAD_EXTENSIONS'] = ['.wav']

def main():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'wav'

# TODO: file uploading for the record button (javascript)
@app.route('/', methods=['GET', 'POST'])
def input():
    error = None
    if request.method == 'POST':
        if 'wav' not in request.files:
            return redirect(request.url)

        wav = request.files.get('wav')
        if not wav:
            return redirect(request.url)
        if wav and allowed_file(wav.filename):
            filename = secure_filename(wav.filename)
            wav_octal = wav.read() # octet-stream type from online?
            wav_bytes = io.BytesIO(wav_octal) # convert to bytes
            sr, audio = scipy.io.wavfile.read(wav_bytes) # audio is numpy array
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            scipy.io.wavfile.write(save_path, sr, audio)
            label = get_prediction(audio)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def get_prediction(wav_bytes):
    return 'missing label'

if __name__=='__main__':
    main()
