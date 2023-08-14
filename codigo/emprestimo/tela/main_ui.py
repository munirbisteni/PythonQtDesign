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

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableEmprestimo = QTableWidget(self.centralwidget)
        if (self.tableEmprestimo.columnCount() < 5):
            self.tableEmprestimo.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableEmprestimo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableEmprestimo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableEmprestimo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableEmprestimo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEmprestimo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableEmprestimo.setObjectName(u"tableEmprestimo")
        self.tableEmprestimo.setGeometry(QRect(90, 161, 591, 161))
        self.textNumeroEmprestimo = QLineEdit(self.centralwidget)
        self.textNumeroEmprestimo.setObjectName(u"textNumeroEmprestimo")
        self.textNumeroEmprestimo.setGeometry(QRect(100, 410, 101, 20))
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
        self.labelNumeroEmprestimo = QLabel(self.centralwidget)
        self.labelNumeroEmprestimo.setObjectName(u"labelNumeroEmprestimo")
        self.labelNumeroEmprestimo.setGeometry(QRect(100, 380, 101, 16))
        self.buttonAdicionar = QPushButton(self.centralwidget)
        self.buttonAdicionar.setObjectName(u"buttonAdicionar")
        self.buttonAdicionar.setGeometry(QRect(520, 120, 75, 23))
        self.labelNumeroLivro = QLabel(self.centralwidget)
        self.labelNumeroLivro.setObjectName(u"labelNumeroLivro")
        self.labelNumeroLivro.setGeometry(QRect(220, 380, 71, 16))
        self.textNumeroLivro = QLineEdit(self.centralwidget)
        self.textNumeroLivro.setObjectName(u"textNumeroLivro")
        self.textNumeroLivro.setGeometry(QRect(220, 410, 71, 20))
        self.textLocatario = QLineEdit(self.centralwidget)
        self.textLocatario.setObjectName(u"textLocatario")
        self.textLocatario.setGeometry(QRect(560, 410, 101, 20))
        self.textNumeroBibliotecaria = QLineEdit(self.centralwidget)
        self.textNumeroBibliotecaria.setObjectName(u"textNumeroBibliotecaria")
        self.textNumeroBibliotecaria.setGeometry(QRect(390, 410, 101, 20))
        self.labelNumeroBibliotecaria = QLabel(self.centralwidget)
        self.labelNumeroBibliotecaria.setObjectName(u"labelNumeroBibliotecaria")
        self.labelNumeroBibliotecaria.setGeometry(QRect(390, 380, 111, 16))
        self.labelLocatario = QLabel(self.centralwidget)
        self.labelLocatario.setObjectName(u"labelLocatario")
        self.labelLocatario.setGeometry(QRect(560, 380, 101, 16))
        self.buttonDevolucao = QPushButton(self.centralwidget)
        self.buttonDevolucao.setObjectName(u"buttonDevolucao")
        self.buttonDevolucao.setGeometry(QRect(370, 450, 151, 23))
        self.buttonDevolucaoNao = QPushButton(self.centralwidget)
        self.buttonDevolucaoNao.setObjectName(u"buttonDevolucaoNao")
        self.buttonDevolucaoNao.setGeometry(QRect(180, 450, 181, 23))
        self.textDevolvido = QLineEdit(self.centralwidget)
        self.textDevolvido.setObjectName(u"textDevolvido")
        self.textDevolvido.setGeometry(QRect(300, 410, 71, 20))
        self.labelNumeroLivro_2 = QLabel(self.centralwidget)
        self.labelNumeroLivro_2.setObjectName(u"labelNumeroLivro_2")
        self.labelNumeroLivro_2.setGeometry(QRect(300, 380, 71, 16))
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableEmprestimo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"numeroEmprestimo", None));
        ___qtablewidgetitem1 = self.tableEmprestimo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"devolucao", None));
        ___qtablewidgetitem2 = self.tableEmprestimo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"numeroLivro", None));
        ___qtablewidgetitem3 = self.tableEmprestimo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"numeroBibliotecario", None));
        ___qtablewidgetitem4 = self.tableEmprestimo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"numeroLocatario", None));
        self.buttonCancelar.setText(QCoreApplication.translate("mainWindow", u"Cancelar", None))
        self.buttonPesquisar.setText(QCoreApplication.translate("mainWindow", u"Pesquisar", None))
        self.buttonSalvar.setText(QCoreApplication.translate("mainWindow", u"Salvar", None))
        self.buttonExcluir.setText(QCoreApplication.translate("mainWindow", u"Excluir", None))
        self.labelNumeroEmprestimo.setText(QCoreApplication.translate("mainWindow", u"N\u00famero Empr\u00e9stimo", None))
        self.buttonAdicionar.setText(QCoreApplication.translate("mainWindow", u"Adicionar", None))
        self.labelNumeroLivro.setText(QCoreApplication.translate("mainWindow", u"N\u00famero Livro", None))
        self.labelNumeroBibliotecaria.setText(QCoreApplication.translate("mainWindow", u"N\u00famero Bibliotec\u00e1rio", None))
        self.labelLocatario.setText(QCoreApplication.translate("mainWindow", u"N\u00famero Locat\u00e1rio", None))
        self.buttonDevolucao.setText(QCoreApplication.translate("mainWindow", u"marcar como devolvido", None))
        self.buttonDevolucaoNao.setText(QCoreApplication.translate("mainWindow", u"marcar como n\u00e3o devolvido", None))
        self.labelNumeroLivro_2.setText(QCoreApplication.translate("mainWindow", u"Devolvido", None))
    # retranslateUi

