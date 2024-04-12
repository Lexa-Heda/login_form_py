import sys, struct, socket
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt6 import QtCore, QtGui, QtWidgets


# pyuic6 first.ui -o first.py
# zum umwandeln von qt designer dateien

class Ui_Login(object):
    def setupUi(self, Login, client):
        self.client = client
        Login.setObjectName("Login")
        Login.resize(353, 451)
        self.login_btn = QtWidgets.QPushButton(parent=Login)
        self.login_btn.setGeometry(QtCore.QRect(100, 290, 111, 31))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.login)
        self.label = QtWidgets.QLabel(parent=Login)
        self.label.setGeometry(QtCore.QRect(20, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Login)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.username_inp = QtWidgets.QLineEdit(parent=Login)
        self.username_inp.setGeometry(QtCore.QRect(100, 130, 113, 22))
        self.username_inp.setObjectName("username_inp")
        self.password_inp = QtWidgets.QLineEdit(parent=Login)
        self.password_inp.setGeometry(QtCore.QRect(100, 190, 113, 22))
        self.password_inp.setObjectName("password_inp")
        self.label_3 = QtWidgets.QLabel(parent=Login)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.register_switch = QtWidgets.QPushButton(parent=Login)
        self.register_switch.setGeometry(QtCore.QRect(120, 330, 75, 24))
        self.register_switch.setAutoRepeatDelay(299)
        self.register_switch.setObjectName("register_switch")
        self.label_error = QtWidgets.QLabel(parent=Login)
        self.label_error.setGeometry(QtCore.QRect(20, 230, 311, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.label_error.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_error.setFont(font)
        self.label_error.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_error.setObjectName("label_error")
        self.label_error.setVisible(False)
        self.output = QtWidgets.QLabel(parent=Login)
        self.output.setGeometry(QtCore.QRect(8, 380, 331, 20))
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output.setObjectName("output")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.login_btn.setText(_translate("Login", "login"))
        self.label.setText(_translate("Login", "Username:"))
        self.label_2.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Password:"))
        self.register_switch.setText(_translate("Login", "register"))
        self.label_error.setText(_translate("Login", "username or password is blank or you are not registered"))

    def login(self):
        print("Login")
        if self.username_inp.text() != "" and self.password_inp.text() != "":
            self.label_error.setVisible(False)
            self.output.setText("")
            data = self.username_inp.text() + "," + self.password_inp.text()
            purpose = "login"
            self.client.send_data(purpose)  # Purpose
            response = self.client.get_response()
            print(response)
            if response == "ok":
                self.client.send_data(data)
                response = self.client.get_response()
                if response:
                    self.output.setText("succesfully logged in")
                else:
                    self.label_error.setVisible(True)

            else:
                self.output.setText("oops, something went wrong...")
        else:
            self.label_error.setVisible(True)

    def register(self):
        pass


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.main_window = Second_Window(self.client)
        self.main_window.show()


class Second_Window(QMainWindow, Ui_Login):
    def __init__(self, client):
        super().__init__()
        print("Initializing Second_Window...")
        self.client = client
        self.setupUi(self, self.client)
        print("Second_Window initialized.")


class Client:
    def __init__(self):
        self.hoster = 'localhost'
        # self.hoster = !<>!
        self.port = 80
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.socket.connect((self.hoster, self.port))

    def close_connection(self):
        self.socket.close()

    def get_response(self):
        data = self.socket.recv(1024).decode()
        print(data)
        return data

    def send_data(self, data):
        if isinstance(data, str):
            self.socket.send(data.encode())
        elif isinstance(data, int):
            encoded_data = struct.pack("i", data)
            self.socket.send(encoded_data)
        elif isinstance(data, list):
            encoded_data = b""
            for item in data:
                if isinstance(item, str):
                    encoded_data += item.encode()
                elif isinstance(item, int):
                    encoded_data += struct.pack("i", item)
            self.socket.send(encoded_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    haupt_fenster = Main_Window()
    sys.exit(app.exec())
