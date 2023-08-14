# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableBibliotecario = QTableWidget(self.centralwidget)
        if (self.tableBibliotecario.columnCount() < 2):
            self.tableBibliotecario.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableBibliotecario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBibliotecario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableBibliotecario.setObjectName(u"tableBibliotecario")
        self.tableBibliotecario.setGeometry(QRect(90, 161, 591, 161))
        self.textNome = QLineEdit(self.centralwidget)
        self.textNome.setObjectName(u"textNome")
        self.textNome.setGeometry(QRect(210, 410, 461, 20))
        self.textCodigo = QLineEdit(self.centralwidget)
        self.textCodigo.setObjectName(u"textCodigo")
        self.textCodigo.setGeometry(QRect(100, 410, 91, 20))
        self.buttonCancelar = QPushButton(self.centralwidget)
        self.buttonCancelar.setObjectName(u"buttonCancelar")
        self.buttonCancelar.setGeometry(QRect(530, 450, 75, 23))
        self.buttonPesquisar = QPushButton(self.centralwidget)
        self.buttonPesquisar.setObjectName(u"buttonPesquisar")
        self.buttonPesquisar.setGeometry(QRect(420, 120, 75, 23))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(100, 350, 571, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.buttonSalvar = QPushButton(self.centralwidget)
        self.buttonSalvar.setObjectName(u"buttonSalvar")
        self.buttonSalvar.setGeometry(QRect(610, 450, 75, 23))
        self.buttonExcluir = QPushButton(self.centralwidget)
        self.buttonExcluir.setObjectName(u"buttonExcluir")
        self.buttonExcluir.setGeometry(QRect(600, 120, 75, 23))
        self.textPesquisar = QLineEdit(self.centralwidget)
        self.textPesquisar.setObjectName(u"textPesquisar")
        self.textPesquisar.setGeometry(QRect(90, 120, 321, 20))
        self.labelNome = QLabel(self.centralwidget)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(210, 380, 47, 13))
        self.labelCodigo = QLabel(self.centralwidget)
        self.labelCodigo.setObjectName(u"labelCodigo")
        self.labelCodigo.setGeometry(QRect(100, 380, 47, 13))
        self.buttonAdicionar = QPushButton(self.centralwidget)
        self.buttonAdicionar.setObjectName(u"buttonAdicionar")
        self.buttonAdicionar.setGeometry(QRect(520, 120, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableBibliotecario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.tableBibliotecario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.buttonCancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.buttonPesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.buttonSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.buttonExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.labelNome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelCodigo.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.buttonAdicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
    # retranslateUi

