"""
¿Qué significa HTML?:HyperText Markup Language
¿Qué significa CSS?:Cascading Style Sheets
¿Qué significa JS?: JavaScript
¿Qué significa DOM?: Document Object Model
¿Qué significa UI?: User Interface
¿Qué es el hosting?: Es el servicio que permite almacenar y publicar un sitio web en Internet.
¿Qué es una página web?: Es un documento electrónico que se muestra en un navegador web y puede contener texto, imágenes, enlaces, etc.
¿Qué es Internet?: Es una red global de computadoras interconectadas que permite la comunicación y el intercambio de información.
¿Qué es el frontend?: Se refiere a la parte de un sitio web que los usuarios ven y con la que interactúan. Incluye HTML, CSS y JavaScript.
¿Qué es el backend?: Se refiere a la parte de un sitio web que está detrás de escena y maneja la lógica y el almacenamiento de datos. Puede incluir servidores y bases de datos.
¿Qué es el modelo cliente-servidor?: Es una arquitectura en la que los clientes (navegadores) solicitan recursos y los servidores (como los servidores web) responden a esas solicitudes.
¿Qué es un servidor web?: Es un programa que recibe solicitudes de los clientes (navegadores) a través de HTTP y envía las respuestas correspondientes, generalmente en forma de páginas web.
¿Qué es un servidor de base de datos?:Es un software que administra el almacenamiento y acceso a una base de datos, permitiendo la gestión de datos de manera eficiente.
"""
preguntas_respuestas = [
    ("¿Qué significa HTML?", "HyperText Markup Language"),
    ("¿Qué significa CSS?", "Cascading Style Sheets"),
    ("¿Qué significa JS?", "JavaScript"),
    ("¿Qué significa DOM?", "Document Object Model"),
    ("¿Qué significa UI?", "User Interface"),
    ("¿Qué es el hosting?", "Es el servicio que permite almacenar y publicar un sitio web en Internet."),
    ("¿Qué es una página web?", "Es un documento electrónico que se muestra en un navegador web y puede contener texto, imágenes, enlaces, etc."),
    ("¿Qué es Internet?", "Es una red global de computadoras interconectadas que permite la comunicación y el intercambio de información."),
    ("¿Qué es el frontend?","Se refiere a la parte de un sitio web que los usuarios ven y con la que interactúan. Incluye HTML, CSS y JavaScript."),
    ("¿Qué es el backend?", "Se refiere a la parte de un sitio web que está detrás de escena y maneja la lógica y el almacenamiento de datos. Puede incluir servidores y bases de datos."),
    ("¿Qué es el modelo cliente-servidor?", "Es una arquitectura en la que los clientes (navegadores) solicitan recursos y los servidores (como los servidores web) responden a esas solicitudes."),
    ("¿Qué es un servidor web?", "Es un programa que recibe solicitudes de los clientes (navegadores) a través de HTTP y envía las respuestas correspondientes, generalmente en forma de páginas web."),
    ("¿Qué es un servidor de base de datos?","Es un software que administra el almacenamiento y acceso a una base de datos, permitiendo la gestión de datos de manera eficiente.")
]

puntuacion = 0

print("¡Bienvenido a juego de conceptos Web!")
print("Si respondes correctamente, sumas puntos!!!.")

for pregunta, respuesta in preguntas_respuestas:
    print("\n" + pregunta)
    respuesta_usuario = input("Respuesta: ")

    if respuesta_usuario.lower() == respuesta.lower():
        print("¡Respuesta correcta!")
        puntuacion += 1
    else:
        print("Respuesta incorrecta. La respuesta correcta es:", respuesta)

print("\nFin del reto")
print("Puntuación obtenida:", puntuacion, "de", len(preguntas_respuestas))
