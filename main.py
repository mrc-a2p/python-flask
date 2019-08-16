# Importo flask
#La objeto request se usa para obtener informacio o datos  
#make_response optiene respuesta del serividor 
# render_template te pinta en el navegador lo que haces en consola
from flask import Flask, request, make_response, redirect, render_template, session
#from flask_bootstrap import Bootstrap
from flask_wtf import  FlaskForm
from wtforms.fields import  StringField, PasswordField, SubmitField
from wtforms.fields import DataRequired


#Crear nueva instancia de flask
app = Flask(__name__)

#inicializamos extenciones de flask
#bootstrap = Bootstrap(app)


# llave secreta 
app.config["SECRET_KEY"] = "SUPER SECRETO" 
############################
# arrays 
#############################

perros = [
    "labrador", 
    "pitbull", 
    "chiwuwa"
]


class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators= [DataRequired ()])
    password = PasswordField("Password", validators= [DataRequired ()])
    submitField = SubmitField("Enviar")

#Control de errores 

@app.errorhandler(404)
def not_found(error):
    return render_template("error-404.html", error=error) 

@app.errorhandler(500)
def internal_server(error):
    return render_template("error-500.html", error=error)  
    #return"Error 500 {}".format(error)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session ["user_ip"] = user_ip

    return response

#Crea ruta y se le pone el nombre deseado 
@app.route("/hello")
# definimos una funcion y le agregamos sus funcionalidades
def hello():
    user_ip = session.get("user_ip")
    #return "Hola mundo,{}" .format(user_ip)
    #Creamos un diccionario con las variables que vamos a utilizar
    login_form = LoginForm()
    context = { 
        "user_ip" : user_ip,
        "perros" : perros,
        "login_form" : login_form
    }

    #renderizamos el codigo en una vista previamente creado en una carpeta de templates 
    #Los asteriscos se deben a que locals() nos regresa un dict con las variables del contexto, pero render_template solo resive un argumento, asi que pasamos el diccionario con key yvaluesen forma de argumentos opcionales. 
    #Esto es util cuando empezamos a tener muchos datos enel entorno.
    #Expande el diccionario e hace un recorrido dato por dato 
    return render_template("hello.html", **context)





###################  mas
@app.route("/marc")
def marc():
    return render_template("marc.html")  


@app.route("/info")
def info():
    #return "lo que sea"
    return render_template("info.html")




################### 
if __name__ == "__main__":
  app.run()
