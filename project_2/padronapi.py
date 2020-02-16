from flask import Flask, render_template, request, jsonify
from flask_api import status
import configparser
import psycopg2

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('padronapi.ini')
cnx=psycopg2.connect(dbname=config['DB']['name'], user=config['DB']['user'], password=config['DB']['password'], host=config['DB']['host'], port=config['DB']['port'])
cur=cnx.cursor()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/api/v1/provincias',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia;")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/provincia/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia WHERE codigo=%s;",(codigo,))
        provincia=cur.fetchone()
        if provincia is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/canton/<string:code_y>/<string:code_x>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def canton(code_y,code_x):
    code_y=str(code_y)
    code_x=str(code_x)	
    canton_x=[]
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE canton.provincia = %s AND canton.codigo = %s;",(code_y, code_x))
        canton_x=cur.fetchone()
        if canton_x is None :
            content = {'Error de código': 'La canton con el código {0} no existe.'.format(code_x)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            data_to_show = {
                'provincia': canton_x[0],
                'codigo': canton_x[1],
                'nombre': canton_x[2]
            }
            return jsonify(data_to_show), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para canton_x'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

@app.route('/api/v1/distrito/<string:provincia_x>/<string:canton_x>/<string:codeX_x>/', methods=['POST', 'GET', 'DELETE', 'PUT'])
def distrito(provincia_x,canton_x,codeX_x):
    code_y=str(provincia_x)
    code_x=str(canton_x)	
    code_z=str(codeX_x)	
    distrito_x=[]
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE distrito.provincia = %s AND distrito.canton = %s AND distrito.codigo = %s;",(code_y, code_x, code_z))
        distrito_x=cur.fetchone()
        if distrito_x is None :
            content = {'Error de código': 'La canton con el código {0} no existe.'.format(code_x)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            data_to_show = {
                'provincia': distrito_x[0],
                'canton': distrito_x[1],
                'codigo': distrito_x[2],                
                'nombre': distrito_x[3]
            }
            return jsonify(data_to_show), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para distrito_x'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED
    
@app.route('/api/v1/personas',methods=['POST', 'GET', 'DELETE', 'PUT'])
def personas():
    if request.method == 'GET':
        cur.execute("SELECT * FROM ciudadano LIMIT '100' OFFSET '0';")
        users = []
        for persona in cur.fetchall():
            data_to_show = {
            'cedula': persona[0],
            'vencimiento': persona[1],
            'sexo': persona[2],
            'nombre': persona[3],
            'apellido1': persona[4],
            'apellido2': persona[5],
            'provincia': persona[6],
            'canton': persona[7],
            'distrito': persona[8],
            'junta': str(persona[9]),
            }
            users.append(data_to_show)
        return jsonify(users), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para personas'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED;
    
if __name__ == '__main__':
    app.debug = True
    app.run()
