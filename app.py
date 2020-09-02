from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

def main():
    app.run(debug=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'wav'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# TODO: save wav to server, then delete from server when delete is pressed
@app.route('/asr', methods=['GET', 'POST'])
def input():
    error = None
    if request.method == 'POST':
        if 'wav' not in request.files:
            return redirect(request.url)

        wav = request.files.get('wav')
        if not wav:
            return redirect(request.url)

        wav_bytes = wav.read()
        label = get_prediction(wav_bytes)

        return render_template('result.html', name='a name', label=label, error=error, wav=wav)

    return render_template('index.html')

def get_prediction(wav_bytes):
    return 'missing label'

if __name__=='__main__':
    main()
