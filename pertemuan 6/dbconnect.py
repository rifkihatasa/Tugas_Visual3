from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Label for database name
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 150, 40))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")

        # LineEdit for database name input
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 40, 300, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("font-size: 14px;")

        # Button to create database
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 120, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("font-size: 14px; padding: 5px;")
        self.pushButton.clicked.connect(self.create_database)

        # Button to connect to database
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 120, 150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("font-size: 14px; padding: 5px;")
        self.pushButton_2.clicked.connect(self.db_connect)

        # Label to display results
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(200, 200, 400, 50))
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setStyleSheet("font-size: 14px; color: green;")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Management"))
        self.label.setText(_translate("MainWindow", "Database Name:"))
        self.pushButton.setText(_translate("MainWindow", "Create Database"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect Database"))
        self.labelResult.setText(_translate("MainWindow", ""))

    def create_database(self):
        """Function to create a database based on input from lineEdit"""
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=""
            )
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            if dbname:  # Check if database name is not empty
                cursor.execute(f"CREATE DATABASE {dbname}")
                self.labelResult.setText(f"Database '{dbname}' created successfully!")
            else:
                self.labelResult.setText("Database name cannot be empty!")
        except mc.Error as e:
            self.labelResult.setText(f"Error creating database: {e}")

    def db_connect(self):
        """Function to connect to a predefined database"""
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            self.labelResult.setText("Successfully connected to 'db_penjualan'")
        except mc.Error as err:
            self.labelResult.setText(f"Error connecting to database: {err}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
