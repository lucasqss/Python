import sys
import json
import jwt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton, QTextEdit

class GUIJWTDecoder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JWT Decoder")
        self.resize(1200, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Enter JWT token:")
        layout.addWidget(self.label)

        self.token_input = QPlainTextEdit()
        self.token_input.setMinimumHeight(50)
        self.token_input.setMaximumHeight(150)
        layout.addWidget(self.token_input)

        self.decode_button = QPushButton("Decode")
        self.decode_button.clicked.connect(self.decode_token)
        layout.addWidget(self.decode_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setMinimumHeight(200)
        # self.result_display.setMaximumHeight(500)
        layout.addWidget(self.result_display)

    def decode_token(self):
        token = self.token_input.toPlainText()
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            self.result_display.setPlainText(json.dumps(decoded, indent=4))
        except jwt.DecodeError as e:
            self.result_display.setPlainText("Error: " + str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUIJWTDecoder()
    window.show()
    sys.exit(app.exec())