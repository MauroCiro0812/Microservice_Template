from flask import Flask,request,jsonify
from microservice import microservice


app = Flask(__name__)

@app.route('/Microservice_facturacion', methods=['GET'])
def microservice_init():

    nit = request.args.get('nit')


    if nit is None or nit == "":
        return jsonify({'error': 'Se requieren los tres parámetros: nit'}), 400
        
    print(nit)
    json_file = microservice.ejecucion(nit)
    return json_file

if __name__=="__main__":
    app.run(debug=True) 