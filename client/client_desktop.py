import sys, struct, socket
import time

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt6 import QtCore, QtGui, QtWidgets

# pyuic6 first.ui -o first.py
# zum umwandeln von qt designer dateien

class Ui_Main(object):
    
    def setupUi(self, Main, client, parent):
        self.server_client = client
        self.parent = parent

        Main.setObjectName("Main")
        Main.setWindowIcon(QtGui.QIcon("icon.png"))
        Main.resize(353, 451)
        self.centralwidget = QtWidgets.QWidget(parent=Main)
        self.centralwidget.setObjectName("centralwidget")
        self.login_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(120, 180, 101, 31))
        self.login_btn.setCheckable(False)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.login)
        self.logout_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logout_btn.setEnabled(True)
        self.logout_btn.setGeometry(QtCore.QRect(130, 270, 75, 24))
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.clicked.connect(self.exit)
        self.label_u1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_u1.setGeometry(QtCore.QRect(40, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_u1.setFont(font)
        self.label_u1.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_u1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_u1.setObjectName("label_u1")
        self.output_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(70, 219, 201, 41))
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 22))
        self.menubar.setObjectName("menubar")
        self.menuConnector = QtWidgets.QMenu(parent=self.menubar)
        self.menuConnector.setObjectName("menuConnector")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConnector.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Simple Login"))
        self.login_btn.setText(_translate("Main", "Login"))
        self.logout_btn.setText(_translate("Main", "logout"))
        self.label_u1.setText(_translate("Main", "Simpler Login"))
        self.menuConnector.setTitle(_translate("Main", "Connector"))

    def login(self):
        print("Login")

        self.switch_to_next_window()
        #self.server_client.connect_to_server()
        #self.server_client.send_data("test") # Purpose
        #time.sleep(0.1)
        #print(self.server_client.get_response())

    def exit(self):
        exit(88)

    def switch_to_next_window(self):
        return True
class Ui_Login(object):
    def setupUi(self, Login, client):
        self.socket = client
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
            data = (self.username_inp.text(), self.password_inp.text())
            self.socket.send_data("login") #Purpose
            response = self.socket.get_response()
            print(response)
            if response == "ok":
                self.socket.send_data(data)
                response = self.socket.get_response()
                if response == True:
                    self.output.setText("succesfully logged in")
                else:
                    self.label_error.setVisible(True)

            else:
                self.output.setText("oops, something went wrong...")
        else:
            self.label_error.setVisible(True)

    def register(self):
        pass


class First_Window(QMainWindow, Ui_Main):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.setupUi(self, self.client, self)

    def show_login_window(self):
        return True

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.main_window = First_Window(self.client)
        self.main_window.show()
        if self.main_window.show_login_window():  # Überprüfung, ob das zweite Fenster angezeigt werden soll
            self.main_window.close()
            self.main_window = Second_Window(self.client)
            self.main_window.show()


    def show_login_window(self):
        # Was soll ich hier als überprüfung reinschreiben
        return True


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
        self.socket.settimeout(5)
        data = self.socket.recv(1024).decode()
        print(data)
        return data

    def send_data(self, data):
        encoded_data = b""
        if isinstance(data, str):
            self.socket.send(data.encode())
        elif isinstance(data, int):
            encoded_data += (struct.pack("i", data))
            self.socket.send(encoded_data)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    encoded_data += (item.encode())
                elif isinstance(item, int):
                    encoded_data += struct.pack("i", item)
            self.socket.send(encoded_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    haupt_fenster = Main_Window()
    sys.exit(app.exec())
