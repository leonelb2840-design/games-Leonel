# Lógica del Servidor y Puente con C++
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# --- BLOQUE DE LÓGICA TIPO C++ ---
# Aquí simulamos la llamada al motor compilado
def motor_de_escaneo_cpp(contenido_binario):
    # En un caso real, aquí llamas a: ctypes.CDLL('./motor.so').analizar()
    # Vamos a simular un escaneo de firmas básico
    if b"VIRUS_DUMMY_CODE" in contenido_binario:
        return "AMENAZA DETECTADA"
    return "ARCHIVO LIMPIO"
# ---------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if 'file' not in request.files:
        return jsonify({"veredicto": "No hay archivo"})
    
    file = request.files['file']
    data = file.read()
    
    # Mandamos los binarios al "C++"
    resultado = motor_de_escaneo_cpp(data)
    
    return jsonify({"veredicto": resultado})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
