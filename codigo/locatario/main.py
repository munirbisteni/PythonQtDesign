from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from tela.main_ui import Ui_MainWindow
import pyodbc
import sys

global database

class Database:

    def __init__(self):
        self.connection = pyodbc.connect(driver = 'SQL Server', server = 'regulus.cotuca.unicamp.br', database = '', uid = '', pwd = '')
        print("entrou no banco de dados!")     

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.list()
        self.disable()
        self.buttonSalvar.clicked.connect(self.save)
        self.buttonCancelar.clicked.connect(self.cancel)
        self.buttonAdicionar.clicked.connect(self.new)
        self.buttonExcluir.clicked.connect(self.delete)
        self.buttonPesquisar.clicked.connect(self.search)

    def disable(self):

        self.textCodigo.setEnabled(not self.textCodigo.isEnabled())
        self.textNome.setEnabled(not self.textNome.isEnabled())

    def clear(self):

        self.textCodigo.setText('')
        self.textNome.setText('')

    def delete(self):

        codigo_locatario = self.tableLocatario.item(self.tableLocatario.currentRow(), 0).text()
        message = QMessageBox(self)
        message.setWindowTitle("Administrar Locatario")
        message.setText("Você gostaria de excluir o Locatario {}?".format(codigo_locatario))
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setIcon(QMessageBox.Warning)
        button = message.exec_()

        if button == QMessageBox.Yes:
            try:
                database.connection.cursor().execute('DELETE FROM biblioteca.Locatario WHERE registro = ?', codigo_locatario)
                database.connection.commit()
                self.list()
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao do Locatario")
                message.setText('O bibliotecário(a) {} foi excluído(a) com sucesso!'.format(codigo_locatario))
                message.setIcon(QMessageBox.Information)
                message.exec()

            except Exception as error:
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao do Locatario")
                message.setText(error.args[0])
                message.setIcon(QMessageBox.Critical)
                message.exec()

    def search(self):

        self.list(self.textPesquisar.text()) 

    def new(self):

        self.disable()

    def save(self):

        try:
            database.connection.cursor().execute('INSERT INTO biblioteca.locatario VALUES (?)',  self.textNome.text())
            database.connection.cursor().commit()
            self.list()
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao do Locatario")
            message.setText('O bibliotecário(a) {} - {} foi incluído(a) com sucesso!'.format(self.textCodigo.text(), self.textNome.text()))
            message.setIcon(QMessageBox.Information)
            message.exec()
            self.disable()
            self.clear() 

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao do Locatario")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()  

    def cancel(self):

        self.disable()
        self.clear()

    def list(self, where = None):

        try:
            if where:
                parameters = ['%' + where + '%', '%' + where + '%']
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.Locatario WHERE registro LIKE ? OR Nome LIKE ?', parameters)
            else:
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.Locatario')
            data = result.fetchall()
            print(data)
            self.tableLocatario.setColumnCount(2)
            self.tableLocatario.setColumnWidth(0, 100)        
            self.tableLocatario.setColumnWidth(1, 200)
            self.tableLocatario.setRowCount(len(data))

            index = 0

            for row in data:
                self.tableLocatario.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.tableLocatario.setItem(index, 1, QTableWidgetItem(str(row[1])))
                index = index + 1

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao do Locatario")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()      
    
        
if __name__ == '__main__':
    database = Database()
    application = QApplication(sys.argv) 
    view = MainWindow()
    view.show()
    application.exec()  