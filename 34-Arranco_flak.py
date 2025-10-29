#Abre una terminal e instala flask
#pip install flask
#Flask es un microservidorweb que nospermite generar HTML desde Python

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    return '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>BryproBLOG</title>
    <style>
        body{background: steelblue; color : steelblue ; font-family:sans-serif;}
        header,main,footer{background: white; padding: 20px; margin: auto; width: 600px;}
        header,footer{text-align: center;}
        main{color: black;}
    </style>
</head>


<body>
    <header><h1>BryproBLOG</h1></header>
    <main>
        <article>
            <h3>Titulo del articulo</h3>
            <time datetime="2025-10-16"></time>
            <p>Bryan Alejandro Avila Castro el Pro</p>
            <p>Este es el contenido de un articulo ficticio</p>
        </article>
    </main>
    <footer>(c)2025 Bryan Alejandor Avila Castro</footer>
</body>
</html>'''

#Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)