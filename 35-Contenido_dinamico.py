#Abre una terminal e instala flask
#pip install flask
#Flask es un microservidorweb que nospermite generar HTML desde Python

from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    
    ###################### Este es otro bloque
    cadena = '''
    <!DOCTYPE html>
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
    '''
        ###################### Este es otro bloque que se repite
    
    archivo = open('35-Blog.json','r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
            <article>
                <h3>'''+linea['Titulo']+'''</h3>
                <time>'''+linea['Fecha']+'''</time>
                <p>'''+linea['Autor']+'''</p>
                <p>'''+linea['contenido']+'''</p>
            </article>
            '''
        ###################### Este es otro bloque
    cadena += '''
    </main>
    <footer>(c)2025 Bryan Alejandro Avila Castro</footer>
</body>
</html>
'''
    ###################### NO OS OLVIDEIS DEL RETURN
    return cadena

#Ahora arranco el servidor
if __name__ == "__main__":
    aplicacion.run(debug=True)