from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return '<h1>Hello World from Python Flask! this is harish </h1>'

app.run(host='0.0.0.0', port=5000)
