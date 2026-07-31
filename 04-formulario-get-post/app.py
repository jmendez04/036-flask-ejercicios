from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]

        return f"""
        <h1>Formulario enviado</h1>

        <p>Hola, <strong>{nombre}</strong>.</p>

        <p>Tu nombre fue recibido correctamente.</p>

        <a href="/">Volver al formulario</a>
        """

    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Formulario GET y POST</title>
    </head>
    <body>
        <h1>Formulario de estudiante</h1>

        <form method="POST">
            <label for="nombre">Nombre:</label>

            <input
                type="text"
                id="nombre"
                name="nombre"
                placeholder="Escribe tu nombre"
                required
            >

            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)