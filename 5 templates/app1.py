from flask import Flask
app = Flask(__name__)

'''
Generating HTML content from Python code is cumbersome
'''

@app.route('/')
def index():
    return "<html><body><h1>Hello World</h1></body></html>"


if __name__ == '__main__':
   app.run(debug = True)
