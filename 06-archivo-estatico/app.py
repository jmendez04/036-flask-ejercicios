from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template(
        "inicio.html",
        titulo="Archivos estáticos en Flask"
    )


if __name__ == "__main__":
    app.run(debug=True)