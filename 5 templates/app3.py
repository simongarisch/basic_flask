from flask import Flask, render_template
app = Flask(__name__)

'''
http://127.0.0.1:5000/hello/51
'''

@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('scores.html', marks=score)


if __name__ == '__main__':
   app.run(debug = True)