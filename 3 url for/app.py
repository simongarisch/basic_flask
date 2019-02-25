'''
The url_for() function is very useful for dynamically building a URL for a specific function.

http://127.0.0.1:5000/admin        --> Hello Admin
http://127.0.0.1:5000/guest/simon  --> Hello simon as Guest
http://127.0.0.1:5000/user/admin   --> Hello Admin
http://127.0.0.1:5000/user/simon   --> Hello simon as Guest
'''

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
   app.run(debug = True)