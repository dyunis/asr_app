from flask import Flask, request, render_template

app = Flask(__name__)

def main():
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/asr', methods=['GET', 'POST'])
def input():
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        f = request.files.get('file')
        if not f:
            error = 'file is None'
        # (read in wav file)
        wav = 0
        return render_template('result.html', name='', description='', error=error)

    return render_template('index.html')

if __name__=='__main__':
    main()
