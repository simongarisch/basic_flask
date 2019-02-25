from flask import Flask, render_template
app = Flask(__name__)

'''
Better to take this approach
http://127.0.0.1:5000/hello/simon  --> Hello simon!

By default, Flask looks in the templates folder in the root level of your app.
The Jinga2 template engine uses the following delimiters for escaping from HTML.

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ##  for Line Statements
'''

@app.route('/hello/<user>')
def hello_name(user):
    return render_template("hello.html", name=user)


if __name__ == '__main__':
    app.run(debug = True)