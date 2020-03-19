#Ronaldo M. Reid 620109753
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
#from werkzeug.utils import secure_filename

csrf = CSRFProtect()

app = Flask(__name__)

# For Flask Form
app.config["SECRET_KEY"] = "9_!Nald&$K8Y{i5*_H3r3}4618542184$@qlShu)_Un3<2gGu57"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgresql:RSK4LFEg@localhost/Users"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
my_db =SQLAlchemy(app)

#For File Upload
#UPLOAD_FOLDER = "./app/static/uploads"
#ALLOWED_EXTENSIONS = {"png", "jpeg", "gif"}
#app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

csrf.init_app(app)
from app import views, models
