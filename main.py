#Importamos flask, request, jsonify
from flask import Flask,request,jsonify
from microservice import microservice


app = Flask(__name__)

#Se declara el End point
@app.route('/api/generacion_factura', methods=['GET'])
def microservice_init():
    #El argumento se convierte en variable
    nit = request.args.get('nit')

    #Si la variable no tiene valor retornameros el mensaje
    if nit is None or nit == "":
        return jsonify({'error': 'Se requieren los tres parámetros: nit'}), 400
        
    print(nit)
    json_file = microservice.ejecucion(nit)
    return json_file

if __name__=="__main__":
    app.run(debug=True) 