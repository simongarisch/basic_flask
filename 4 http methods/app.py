'''
Http protocol is the foundation of data communication in world wide web.
Different methods of data retrieval from specified URL are defined in this protocol.

Open login.html in your browser
'''

from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug = True)
