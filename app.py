import os

from flask import Flask, request, render_template, redirect, send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 3

def main():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'wav'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# TODO: file uploading for the record button (javascript)
@app.route('/asr', methods=['GET', 'POST'])
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
            wav.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            wav_bytes = wav.read()
            label = get_prediction(wav_bytes)

            return render_template('result.html', name='a name', label=label, error=error, wav=os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def get_prediction(wav_bytes):
    return 'missing label'

if __name__=='__main__':
    main()
