# PyChrome

# Importamos las librerias necesarias
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl


class PyChrome(QWidget):
    def __init__(self):
        super().__init__()

        # Comenzamos definiendo algunas caracteristicas de la ventana
        self.resize(740, 520) # Tamaño de la ventana
        self.setWindowTitle('PyChrome') # Titulo de la ventana


        # Creamos la barra de busqueda
        page = "https://www.google.com" # la variable page sera el texto por defecto
        self.url = QLineEdit(page)
        self.url.setPlaceholderText(page)

        # Creamos el boton que iniciara la busqueda
        self.go = QPushButton("Ir")
        self.go.clicked.connect(self.btnIrClicked)

        # Generamos un QHBoxLayout y agregamos los widget creados anteriormente
        self.nav_bar = QHBoxLayout()
        self.nav_bar.addWidget(self.url)
        self.nav_bar.addWidget(self.go)

        # Barra de progreso
        self.progress = QProgressBar()
        self.progress.setValue(0)

        # Cuerpo HTML que mostraremos al iniciar la pagina
        html = """
        <!DOCTYPE HTML>
            <html>
                <head>
                    <title>PyChrome</title>
                </head>
                <body>
                <style>
                    *{
                    font-family: Arial;
                    }
                </style>
                    <h1>Bienvenido a PyChrome</h1>
                    <img src=""/>
                    <p>PyChrome es un navegador web creado por Luis Salcedo
                     y promocionado por <a href="www.pythondiario.com">Mi Diario Python</a>.</p>
                </body>
            </html>
        """

        # Asignamos el cuerpo HTML por defecto que hemos escrito
        self.web_view = QWebEngineView() 
        self.web_view.loadProgress.connect(self.webLoading)
        self.web_view.setHtml(html)

        # Creamos un QVBoxLayout y agregamos la barra de navegación, el cuadro de la pagina y la barra de progreso
        root = QVBoxLayout()
        root.addLayout(self.nav_bar)
        root.addWidget(self.web_view)
        root.addWidget(self.progress)
        self.setLayout(root)

    # Creamos una función que sera la que hara la busqueda de la pagina
    def btnIrClicked(self, event):
        url = QUrl(self.url.text())
        self.web_view.page().load(url)

    # Actualizamos el valor de la barra de progreso
    def webLoading(self, event):
        self.progress.setValue(event)


if __name__ == '__main__':
    # Creamos la instancia de la clase creada y mostramos la ventana en pantalla
    app = QApplication(sys.argv)
    win = PyChrome()
    win.show()
    sys.exit(app.exec_())