#Importacion de librerias de la aplicacion
from fileinput import filename
import re
from flask import Flask
from flask import render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os 

#Se crea la aplicacion Flask
app = Flask(__name__)

#Configuracion acceso a base de datos Mariadb
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='solicitudes'
mysql.init_app(app)

#Ruteo para la carpeta de subidas del usuario
CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA

#Ruteo para guardar las fotos en el directorio uploads
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)

@app.route('/index')
def index():

    sql ="SELECT * FROM `registro`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)

    registro=cursor.fetchall()
    print(registro)

    conn.commit()

    return render_template('registros/index.html', registro=registro)

@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT foto FROM registro WHERE id=%s", id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
 

    cursor.execute("DELETE FROM registro WHERE id = %s",(id))
    conn.commit()
    return redirect('/index')

@app.route('/edit/<int:id>')
def edit(id):

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registro WHERE id = %s", (id))
    registros=cursor.fetchall()
    conn.commit()
    print(registros)

    return render_template('registros/edit.html', registros=registros)

@app.route('/update', methods=['POST'])
def update():
    _cedula=request.form['txtCedula']
    _lugarExpedicion=request.form['txtLugarExpedicion']
    _nombres=request.form['txtNombres']
    _apellidos=request.form['txtApellidos']
    _telefono=request.form['txtTelefono']
    _email=request.form['txtEmail']
    _empresaLaboro=request.form['txtEmpresaLaboro']
    _cargo=request.form['txtCargo']
    _fechaInicio=request.form['txtFechaInicio']
    _fechaRetiro=request.form['txtFechaRetiro']
    _fechaNacimiento=request.form['txtFechaNacimiento']
    _fondoPension=request.form['txtFondoPension']
    _foto=request.files['txtFoto']    
    id=request.form['txtID']
    _estado=request.form['txtEstadoSolicitud']
    _notas=request.form['txtNotas']


    sql ="UPDATE `registro` SET cedula=%s, lugarExpedicion=%s, nombres=%s, apellidos=%s, telefono=%s, email=%s, empresaLaboro=%s, cargo=%s, fechaInicio=%s, fechaRetiro=%s, fechaNacimiento=%s, fondoPension=%s, estado=%s, notas=%s WHERE id=%s ;"
    
    datos=(_cedula,_lugarExpedicion,_nombres,_apellidos,_telefono,_email,_empresaLaboro,_cargo,_fechaInicio,_fechaRetiro,_fechaNacimiento,_fondoPension, _estado, _notas, id)
    
    conn = mysql.connect()
    cursor = conn.cursor()

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename!='':

        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)

        cursor.execute("SELECT foto FROM registro WHERE id=%s", id)
        fila=cursor.fetchall()

        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        cursor.execute("UPDATE registro SET foto=%s WHERE id=%s",(nuevoNombreFoto,id)) 
        conn.commit()   

    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/index')

@app.route('/create')
def create():
    return render_template('registros/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _cedula=request.form['txtCedula']
    _lugarExpedicion=request.form['txtLugarExpedicion']
    _nombres=request.form['txtNombres']
    _apellidos=request.form['txtApellidos']
    _telefono=request.form['txtTelefono']
    _email=request.form['txtEmail']
    _empresaLaboro=request.form['txtEmpresaLaboro']
    _cargo=request.form['txtCargo']
    _fechaInicio=request.form['txtFechaInicio']
    _fechaRetiro=request.form['txtFechaRetiro']
    _fechaNacimiento=request.form['txtFechaNacimiento']
    _fondoPension=request.form['txtFondoPension']
    _foto=request.files['txtFoto']
    _estado=request.form['txtEstadoSolicitud']
    _notas=request.form['txtNotas']

    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if _foto.filename!='':
        nuevoNombreFoto=tiempo+_foto.filename
        _foto.save("uploads/"+nuevoNombreFoto)

    sql ="INSERT INTO `registro` (`id`, `cedula`, `lugarExpedicion`, `nombres`, `apellidos`, `telefono`, `email`, `empresaLaboro`, `cargo`, `fechaInicio`, `fechaRetiro`, `fechaNacimiento`, `fondoPension`, `foto`, `estado`, `notas`) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    
    datos=(_cedula,_lugarExpedicion,_nombres,_apellidos,_telefono,_email,_empresaLaboro,_cargo,_fechaInicio,_fechaRetiro,_fechaNacimiento,_fondoPension,nuevoNombreFoto,_estado,_notas)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/index')



@app.route('/')
def loggin():
    return render_template('Inicio.html')

@app.route('/registro')
def registro():
    return render_template('Registro.html')

@app.route("/error")
def errorConexion():
    return render_template('ErrorConexion.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def Autenticate():

    username = request.form['u']
    password = request.form['p']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM User WHERE username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
        return render_template('ErrorConexion.html')
    else:
        return render_template('registros/home.html')

@app.route('/autentication', methods=['POST'])
def autentication():
    _usuario=request.form['txtUsuario']
    _contrase??a=request.form['txtContrase??a']

    sql ="INSERT INTO `User` (`username`, `password`) VALUES (%s,%s);"
    
    datos=(_usuario,_contrase??a)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run()