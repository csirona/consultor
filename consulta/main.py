from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Configura tu API
API_URL1 = "https://spu.a.pinggy.link/f_mater/{code}"
API_URL2 = "https://spu.a.pinggy.link/f_mater_1/{code}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    producto = request.form['producto']
    # Ajusta el parámetro para que coincida con la estructura de la URL
    headers = {'x-api-key':'c60d0695a78595a9ccc4c9e95d6ab12a13fe9a0fce8e7f4ee322c85480b92b4d'}
    response = requests.get(f'https://spu.a.pinggy.link/f_mater/{producto}')
    response2 = requests.get(f'https://spu.a.pinggy.link/f_mater_1/{producto}')
    data = response.json()
    data2 = response2.json()

    print('asas')
    print(data[2])
    print(data2[14])
    precio = data2[14]
    nombre = data[2]
    return jsonify({'producto': producto, 'precio': precio,'nombre':nombre})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

