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
        
if __name__ == '__main__':
    app.debug = True
    app.run()
