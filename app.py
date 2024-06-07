from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacion = request.form['operacion']

        if operacion == 'sumar':
            resultado = num1 + num2
            resultado = "Maquinola"
        elif operacion == 'restar':
            resultado = num1 - num2
            resultado = "Maquinola"
        elif operacion == 'multiplicar':
            resultado = num1 * num2
            resultado = "Maquinola"
        elif operacion == 'dividir':
            if num2 != 0:
                resultado = num1 / num2 
                resultado = "Maquinola"
            else:
                resultado = 'Error: No se puede dividir por cero (boludoooo)'
        else:
            resultado = 'Operación no válida (o sea man jijo)'

        return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
