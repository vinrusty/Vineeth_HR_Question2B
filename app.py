from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Vineeth H R 1BM20IS183!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
