import flask

def main():
    app = Flask(__name__)
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def input():
    if flask.request.method == 'POST':
        if 'file' not in flask.request.files:
            return redirect(flask.request.url)
        f = flask.request.files.get('file')
        if not f:
            return
        # (read in wav file)
        wav = 0
        return flask.render_template('result.html', name=, description=)

    return flask.render_template('index.html')

if __name__=='__main__':
    main()
