from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <h1>Ejercicio 7</h1>

    <p>
        <a href="/contacto">
            Abrir formulario de contacto
        </a>
    </p>
    """


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]

        return render_template(
            "agradecimiento.html",
            nombre=nombre,
            mensaje=mensaje
        )

    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)