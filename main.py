# Importo flask
#La objeto request se usa para obtener informacio o datos  
#make_response optiene respuesta del serividor 
# render_template te pinta en el navegador lo que haces en consola
from flask import Flask, request, make_response, redirect, render_template

#Crear nueva instancia de flask
app = Flask(__name__)


############################
# Creación de rutas 
#############################
@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)

    return response

#Crea ruta y se le pone el nombre deseado 
@app.route("/hello")
# definimos una funcion y le agregamos sus funcionalidades
def hello():
    user_ip = request.cookies.get("user_ip")
    #return "Hola mundo,{}" .format(user_ip)
    #renderizamos el codigo en una vista previamente creado en una carpeta de templates 
    return render_template("hello.html", user_ip=user_ip)

@app.route("/marc")
def marc():
    return render_template("marc.html")  
