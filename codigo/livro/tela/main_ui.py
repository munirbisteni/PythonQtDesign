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
        self.tableLivro = QTableWidget(self.centralwidget)
        if (self.tableLivro.columnCount() < 6):
            self.tableLivro.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableLivro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableLivro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableLivro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableLivro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableLivro.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableLivro.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableLivro.setObjectName(u"tableLivro")
        self.tableLivro.setGeometry(QRect(90, 111, 591, 161))
        self.textCodigo = QLineEdit(self.centralwidget)
        self.textCodigo.setObjectName(u"textCodigo")
        self.textCodigo.setGeometry(QRect(100, 360, 101, 20))
        self.buttonCancelar = QPushButton(self.centralwidget)
        self.buttonCancelar.setObjectName(u"buttonCancelar")
        self.buttonCancelar.setGeometry(QRect(530, 490, 75, 23))
        self.buttonPesquisar = QPushButton(self.centralwidget)
        self.buttonPesquisar.setObjectName(u"buttonPesquisar")
        self.buttonPesquisar.setGeometry(QRect(420, 70, 75, 23))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(100, 300, 571, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.buttonSalvar = QPushButton(self.centralwidget)
        self.buttonSalvar.setObjectName(u"buttonSalvar")
        self.buttonSalvar.setGeometry(QRect(610, 490, 75, 23))
        self.buttonExcluir = QPushButton(self.centralwidget)
        self.buttonExcluir.setObjectName(u"buttonExcluir")
        self.buttonExcluir.setGeometry(QRect(600, 70, 75, 23))
        self.textPesquisar = QLineEdit(self.centralwidget)
        self.textPesquisar.setObjectName(u"textPesquisar")
        self.textPesquisar.setGeometry(QRect(90, 70, 321, 20))
        self.labelCodigo = QLabel(self.centralwidget)
        self.labelCodigo.setObjectName(u"labelCodigo")
        self.labelCodigo.setGeometry(QRect(100, 330, 101, 16))
        self.buttonAdicionar = QPushButton(self.centralwidget)
        self.buttonAdicionar.setObjectName(u"buttonAdicionar")
        self.buttonAdicionar.setGeometry(QRect(520, 70, 75, 23))
        self.labelTitulo = QLabel(self.centralwidget)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setGeometry(QRect(220, 330, 71, 16))
        self.textTitulo = QLineEdit(self.centralwidget)
        self.textTitulo.setObjectName(u"textTitulo")
        self.textTitulo.setGeometry(QRect(220, 360, 451, 20))
        self.textISBN = QLineEdit(self.centralwidget)
        self.textISBN.setObjectName(u"textISBN")
        self.textISBN.setGeometry(QRect(270, 430, 101, 20))
        self.textPrateleira = QLineEdit(self.centralwidget)
        self.textPrateleira.setObjectName(u"textPrateleira")
        self.textPrateleira.setGeometry(QRect(100, 430, 141, 20))
        self.labelPrateleira = QLabel(self.centralwidget)
        self.labelPrateleira.setObjectName(u"labelPrateleira")
        self.labelPrateleira.setGeometry(QRect(100, 400, 111, 16))
        self.labelISBN = QLabel(self.centralwidget)
        self.labelISBN.setObjectName(u"labelISBN")
        self.labelISBN.setGeometry(QRect(270, 400, 101, 16))
        self.textAutor = QLineEdit(self.centralwidget)
        self.textAutor.setObjectName(u"textAutor")
        self.textAutor.setGeometry(QRect(400, 430, 271, 20))
        self.labelAutor = QLabel(self.centralwidget)
        self.labelAutor.setObjectName(u"labelAutor")
        self.labelAutor.setGeometry(QRect(400, 400, 71, 16))
        self.labelGenero = QLabel(self.centralwidget)
        self.labelGenero.setObjectName(u"labelGenero")
        self.labelGenero.setGeometry(QRect(100, 460, 111, 16))
        self.textGenero = QLineEdit(self.centralwidget)
        self.textGenero.setObjectName(u"textGenero")
        self.textGenero.setGeometry(QRect(100, 490, 61, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableLivro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NumeroLivro", None));
        ___qtablewidgetitem1 = self.tableLivro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem2 = self.tableLivro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Prateleira", None));
        ___qtablewidgetitem3 = self.tableLivro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem4 = self.tableLivro.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem5 = self.tableLivro.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"IdGenero", None));
        self.buttonCancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.buttonPesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.buttonSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.buttonExcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.labelCodigo.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Livro", None))
        self.buttonAdicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.labelTitulo.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.textPrateleira.setText("")
        self.labelPrateleira.setText(QCoreApplication.translate("MainWindow", u"Prateleira", None))
        self.labelISBN.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.labelAutor.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.labelGenero.setText(QCoreApplication.translate("MainWindow", u"IdGenero", None))
        self.textGenero.setText("")
    # retranslateUi

