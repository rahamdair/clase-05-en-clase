from flask import Flask, request, jsonify, render_template
from metodos import load_models, predict

app = Flask(__name__)

@app.route('/prediccion', methods=['POST', 'GET'])
def prediccion(mensaje=None):
    """
    """
    mensaje = request.args.get('mensaje')
    print(mensaje)

    vectoriser, LRmodel = load_models()
    valor = predict(vectoriser, LRmodel, mensaje)
    return jsonify({'prediction': valor})


@app.route('/', methods=('GET', 'POST'))
def prediccion_formulario():
    valor_prediccion = None
    tipo_prediccion = -1
    if request.method == 'POST':
        mensaje = request.form['mensaje']
        print(mensaje)
        if len(mensaje) >0:
            vectoriser, LRmodel = load_models()
            tipo_prediccion, valor_prediccion = predict(vectoriser, LRmodel, mensaje)
        else:
            valor_prediccion = "Sin procesar"        
    return render_template('index.html', valor_prediccion=valor_prediccion,
                           tipo_prediccion=tipo_prediccion)


if __name__ == '__main__':
    app.run(port=8080)
