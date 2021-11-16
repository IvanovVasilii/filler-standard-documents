# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\vasiva\PycharmProjects\Document_optimization_GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCatalog = QtWidgets.QPushButton(self.centralwidget)
        self.btnCatalog.setObjectName("btnCatalog")
        self.gridLayout.addWidget(self.btnCatalog, 2, 1, 1, 1)
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setObjectName("lblResult")
        self.gridLayout.addWidget(self.lblResult, 5, 0, 1, 1)
        self.lineEditCatalog = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCatalog.setObjectName("lineEditCatalog")
        self.gridLayout.addWidget(self.lineEditCatalog, 2, 0, 1, 1)
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 7, 0, 1, 2)
        self.lineEditTemplate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTemplate.setObjectName("lineEditTemplate")
        self.gridLayout.addWidget(self.lineEditTemplate, 4, 0, 1, 1)
        self.btnResult = QtWidgets.QPushButton(self.centralwidget)
        self.btnResult.setObjectName("btnResult")
        self.gridLayout.addWidget(self.btnResult, 6, 1, 1, 1)
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setObjectName("lineEditResult")
        self.gridLayout.addWidget(self.lineEditResult, 6, 0, 1, 1)
        self.lblTemplate = QtWidgets.QLabel(self.centralwidget)
        self.lblTemplate.setObjectName("lblTemplate")
        self.gridLayout.addWidget(self.lblTemplate, 3, 0, 1, 1)
        self.lblCatalog = QtWidgets.QLabel(self.centralwidget)
        self.lblCatalog.setObjectName("lblCatalog")
        self.gridLayout.addWidget(self.lblCatalog, 0, 0, 1, 1)
        self.btnTemplate = QtWidgets.QPushButton(self.centralwidget)
        self.btnTemplate.setObjectName("btnTemplate")
        self.gridLayout.addWidget(self.btnTemplate, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sisyphus"))
        self.btnCatalog.setText(_translate("MainWindow", "Изменить"))
        self.lblResult.setText(_translate("MainWindow", "Папка для сохранения полученных файлов:"))
        self.btnStart.setText(_translate("MainWindow", "Старт"))
        self.btnResult.setText(_translate("MainWindow", "Изменить"))
        self.lblTemplate.setText(_translate("MainWindow", "Папка с шаблонами:"))
        self.lblCatalog.setText(_translate("MainWindow", "Файл-каталог с информацией для заполнения шаблонов:"))
        self.btnTemplate.setText(_translate("MainWindow", "Изменить"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblResultMessage = QtWidgets.QLabel(Dialog)
        self.lblResultMessage.setObjectName("lblResultMessage")
        self.verticalLayout.addWidget(self.lblResultMessage)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Результаты работы утилиты"))
        self.lblResultMessage.setText(_translate("Dialog", "TextLabel"))
        self.btnOk.setText(_translate("Dialog", "Открыть папку"))
