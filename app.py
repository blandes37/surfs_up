from flask import Flask

app = Flask(__name__)
@app.route('/')
def heelo_world():
    return 'Hello world'
