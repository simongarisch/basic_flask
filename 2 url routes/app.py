from flask import Flask
app = Flask(__name__)

''''
http://127.0.0.1:5000/             --> Index!
http://127.0.0.1:5000/hello        --> Hello World!
http://127.0.0.1:5000/members      --> Members
http://127.0.0.1:5000/hello/Simon  --> Hello Simon!
http://127.0.0.1:5000/blog/3       --> Blog Number 3
http://127.0.0.1:5000/rev/7.7      --> Revision Number 7.7
'''

 
@app.route("/")
def index():
    return "Index!"
 
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
 
@app.route("/members")
def members():
    return "Members"


@app.route('/hello/<name>')
def hello_name(name):
    return "Hello %s!" % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo


if __name__ == "__main__":
    app.run()