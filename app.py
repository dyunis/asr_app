from flask import Flask, request, render_template

app = Flask(__name__)

def main():
    app.run(debug=True)

@app.route('/')
def index():
    return f'{[1, 3, 4]} this is the index'

@app.route('/hello')
def hello_world():
    return 'Hello, World'

# the path in app.route generates the html file path for the webapp

# @app.route('/', methods=['GET', 'POST'])
# def input():
    # if request.method == 'POST':
        # if 'file' not in request.files:
            # return redirect(request.url)
        # f = request.files.get('file')
        # if not f:
            # return
        # # (read in wav file)
        # wav = 0
        # return render_template('result.html', name=, description=)
# 
    # return render_template('index.html')

if __name__=='__main__':
    main()
