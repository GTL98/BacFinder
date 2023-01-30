# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacebiyqBh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QSize(600, 450))
        MainWindow.setMaximumSize(QSize(600, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/icones/icones/clipart1887830.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.linha_arquivo_pdf = QLineEdit(self.centralwidget)
        self.linha_arquivo_pdf.setObjectName(u"linha_arquivo_pdf")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.linha_arquivo_pdf.setFont(font2)

        self.horizontalLayout.addWidget(self.linha_arquivo_pdf)

        self.botao_pdf = QPushButton(self.centralwidget)
        self.botao_pdf.setObjectName(u"botao_pdf")
        self.botao_pdf.setFont(font2)
        self.botao_pdf.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icones/icones/abrir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_pdf.setIcon(icon1)

        self.horizontalLayout.addWidget(self.botao_pdf)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.linha_arquivo_bacterias = QLineEdit(self.centralwidget)
        self.linha_arquivo_bacterias.setObjectName(u"linha_arquivo_bacterias")
        self.linha_arquivo_bacterias.setFont(font2)

        self.horizontalLayout_2.addWidget(self.linha_arquivo_bacterias)

        self.botao_txt = QPushButton(self.centralwidget)
        self.botao_txt.setObjectName(u"botao_txt")
        self.botao_txt.setFont(font2)
        self.botao_txt.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icones/icones/criar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_txt.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.botao_txt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.linha_bacterias = QLineEdit(self.centralwidget)
        self.linha_bacterias.setObjectName(u"linha_bacterias")
        self.linha_bacterias.setFont(font2)

        self.horizontalLayout_3.addWidget(self.linha_bacterias)

        self.botao_executar = QPushButton(self.centralwidget)
        self.botao_executar.setObjectName(u"botao_executar")
        self.botao_executar.setFont(font2)
        self.botao_executar.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icones/icones/executar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_executar.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.botao_executar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lista_bacterias = QPlainTextEdit(self.centralwidget)
        self.lista_bacterias.setObjectName(u"lista_bacterias")
        self.lista_bacterias.setFont(font2)

        self.verticalLayout.addWidget(self.lista_bacterias)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.botao_salvar = QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName(u"botao_salvar")
        self.botao_salvar.setFont(font2)
        self.botao_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icones/icones/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_salvar.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.botao_salvar)

        self.botao_excluir = QPushButton(self.centralwidget)
        self.botao_excluir.setObjectName(u"botao_excluir")
        self.botao_excluir.setFont(font2)
        self.botao_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icones/icones/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botao_excluir.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.botao_excluir)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"BacFinder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Arquivo PDF:", None))
        self.botao_pdf.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Arquivo bact\u00e9rias:", None))
        self.botao_txt.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bact\u00e9rias:", None))
        self.botao_executar.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.botao_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
    # retranslateUi

