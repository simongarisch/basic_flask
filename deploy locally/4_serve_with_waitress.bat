cd app
call "./appenv/Scripts/activate"
pip install waitress

@echo off
echo from waitress import serve> waitress_server.py
echo import index>> waitress_server.py
echo[ >> waitress_server.py
echo if __name__ == '__main__':>> waitress_server.py
echo    serve(index.app, host='0.0.0.0', port=81)>> waitress_server.py
