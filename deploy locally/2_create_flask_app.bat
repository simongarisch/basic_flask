cd app
@echo off

echo from flask import Flask> index.py 
echo app = Flask(__name__)>> index.py
echo[ >> index.py
echo @app.route('/')>> index.py
echo def hello():>> index.py
echo    return 'Hello World!' >> index.py
echo[ >> index.py
echo if __name__ == '__main__':>> index.py
echo    app.run()>> index.py
