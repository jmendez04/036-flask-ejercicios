from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():

    return f"""
    
    <h1>ParametrosURL</h1>
    <p>Hola debes escribir tu nombre en el url seguido de un <strong>/</strong></p>
    <p>Ejemplo:</p>
    <p>http://127.0.0.1:5000<strong>/estudiante/Jonatan</strong>
"""

@app.route("/estudiante/<nombre>")
def estudiante(nombre):
    return f"""

    <h1>Bienvenido</h1>
    <p>Hola <strong>{nombre}</strong>.</p>
"""

if __name__=="__main__":
    app.run(debug=True)