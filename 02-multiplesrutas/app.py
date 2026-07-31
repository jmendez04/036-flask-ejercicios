from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Bienvenido a la página principal. Las rutas son: /contactos & /cursos" 


@app.route("/contacto")
def contacto():
    return "Esta es la página de contacto."


@app.route("/cursos")
def cursos():
    return "Cursos disponibles: HTML, CSS, Python y Flask."


if __name__ == "__main__":
    app.run(debug=True)