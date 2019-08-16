//
python3 -m venv venv
virtualenv venv

//
. venv/bin/activate
source bin/activate
source venv/bin/activate

//
export FLASK_APP=main.py
export FLASK_DEBUG=1
//
export FLASK_APP=flaskr
export FLASK_ENV=development


//
pip install -r requirements.txt

//
flask run


//

pip install -r requirements.txt --ignore-installed

pip install Flask
pip install Flask twilio
pip install python-dotenv
//
python --version


#export FLASK_APP="flaskr.factory:create_app()"


