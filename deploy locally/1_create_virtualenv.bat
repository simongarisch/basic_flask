REM pip install virtualenv
call activate py36
mkdir app
cd app
call virtualenv appenv
call "./appenv/Scripts/activate"
pip install flask

