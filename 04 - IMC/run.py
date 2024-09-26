from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    categoria = None
    if request.method == 'POST':
        peso = request.form.get('peso', type=float)
        altura = request.form.get('altura', type=float)
        if peso and altura:
            resultado = peso / (altura ** 2)
            resultado = round(resultado, 2)
            categoria = calcular_categoria_imc(resultado)
    return render_template('index.html', resultado=resultado, categoria=categoria)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)