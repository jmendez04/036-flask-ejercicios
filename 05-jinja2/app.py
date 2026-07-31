from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    nombre = "Jonatan Méndez"
    curso = "Desarrollo Web"

    return render_template(
        "inicio.html",
        estudiante=nombre,
        nombre_curso=curso
    )


if __name__ == "__main__":
    app.run(debug=True)