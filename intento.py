import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de ejemplo")

        # Crear el widget central y el layout principal
        central_widget = QWidget(self)
        main_layout = QHBoxLayout(central_widget)
        central_widget.setLayout(main_layout)

        # Crear el layout para la sección del usuario
        user_layout = QVBoxLayout()
        main_layout.addLayout(user_layout)

        # Nombre de usuario
        username_label = QLabel("Nombre de usuario:")
        user_layout.addWidget(username_label)
        username_text = QLineEdit()
        user_layout.addWidget(username_text)

        # Imagen
        image_label = QLabel("Imagen:")
        user_layout.addWidget(image_label)
        # Aquí puedes agregar tu propio widget para mostrar la imagen

        # Descripción
        description_label = QLabel("Descripción:")
        user_layout.addWidget(description_label)
        description_text = QLineEdit()
        user_layout.addWidget(description_text)

        # Crear el layout para la sección de atributos
        attributes_layout = QGridLayout()
        main_layout.addLayout(attributes_layout)

        # Datos ficticios para las filas de atributos
        attributes = [
            ("Atributo 1:", "Valor 1"),
            ("Atributo 2:", "Valor 2"),
            ("Atributo 3:", "Valor 3"),
            ("Atributo 4:", "Valor 4"),
            ("Atributo 5:", "Valor 5"),
            ("Atributo 6:", "Valor 6")
        ]

        # Agregar las filas de atributos
        for row, (attribute, value) in enumerate(attributes):
            attribute_label = QLabel(attribute)
            value_label = QLabel(value)

            attributes_layout.addWidget(attribute_label, row, 0)
            attributes_layout.addWidget(value_label, row, 1)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
