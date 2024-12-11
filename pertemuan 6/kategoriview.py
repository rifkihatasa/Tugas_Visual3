from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Kategori(object):
    def setupUi(self, Kategori):
        Kategori.setObjectName("Kategori")
        Kategori.resize(463, 481)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonInsert.setFont(font)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 10, 281, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.lineEditId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditId.setFont(font)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout.addWidget(self.lineEditId)

        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout.addWidget(self.lineEditName)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 151, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.labelId = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelId.setFont(font)
        self.labelId.setObjectName("labelId")
        self.verticalLayout_2.addWidget(self.labelId)

        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_2.addWidget(self.labelName)

        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(10, 160, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 200, 441, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 420, 441, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButtonLoad = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonLoad.setFont(font)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout_2.addWidget(self.pushButtonLoad)

        # Connect buttons to functions
        self.pushButtonInsert.clicked.connect(self.insertkategori)
        self.pushButtonLoad.clicked.connect(self.loadkategori)

        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            cursor = mydb.cursor()
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()
            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namekat)
            cursor.execute(sql, val)
            mydb.commit()
            self.labelResult.setText("Data Kategori Berhasil Disimpan")
            self.lineEditId.clear()
            self.lineEditName.clear()
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def loadkategori(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT id, name FROM kategori ORDER BY id ASC")
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.labelResult.setText("Data Kategori Berhasil Ditampilkan")
        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form Kategori"))
        self.pushButtonInsert.setText(_translate("Kategori", "INSERT DATA"))
        self.labelId.setText(_translate("Kategori", "ID Kategori"))
        self.labelName.setText(_translate("Kategori", "Nama Kategori"))
        self.labelResult.setText(_translate("Kategori", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Kategori", "ID Kategori"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Kategori", "Nama Kategori"))
        self.pushButtonLoad.setText(_translate("Kategori", "LOAD DATA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())
