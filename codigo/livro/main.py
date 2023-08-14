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
        self.textTitulo.setEnabled(not self.textTitulo.isEnabled())
        self.textPrateleira.setEnabled(not self.textPrateleira.isEnabled())
        self.textISBN.setEnabled(not self.textISBN.isEnabled())
        self.textAutor.setEnabled(not self.textAutor.isEnabled())
        self.textGenero.setEnabled(not self.textGenero.isEnabled())

    def clear(self):

        self.textCodigo.setText('')
        self.textTitulo.setText('')
        self.textPrateleira.setText('')
        self.textISBN.setText('')
        self.textAutor.setText('')
        self.textGenero.setText('')


    def delete(self):

        codigo_livro = self.tableLivro.item(self.tableLivro.currentRow(), 0).text()
        message = QMessageBox(self)
        message.setWindowTitle("Administrar Livro")
        message.setText("Você gostaria de excluir o Livro {}?".format(codigo_livro))
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setIcon(QMessageBox.Warning)
        button = message.exec_()

        if button == QMessageBox.Yes:
            try:
                database.connection.cursor().execute('DELETE FROM biblioteca.livro WHERE NumeroLivro = ?', codigo_livro)
                database.connection.commit()
                self.list()
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao dos Livros")
                message.setText('O Livro {} foi excluído com sucesso!'.format(codigo_livro))
                message.setIcon(QMessageBox.Information)
                message.exec()

            except Exception as error:
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao dos Livros")
                message.setText(error.args[0])
                message.setIcon(QMessageBox.Critical)
                message.exec()

    def search(self):

        self.list(self.textPesquisar.text()) 

    def new(self):

        self.disable()

    def save(self):

        try:
            database.connection.cursor().execute('INSERT INTO biblioteca.livro VALUES (?,?,?,?,?)',  self.textTitulo.text(), self.textPrateleira.text(),self.textISBN.text(),self.textAutor.text(),self.textGenero.text())
            database.connection.cursor().commit()
            self.list()
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Livros")
            message.setText('O Livro {} - {} foi incluído com sucesso!'.format(self.textCodigo.text(), self.textTitulo.text()))
            message.setIcon(QMessageBox.Information)
            message.exec()
            self.disable()
            self.clear() 

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Livros")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()  

    def cancel(self):

        self.disable()
        self.clear()

    def list(self, where = None):

        try:
            if where:
                parameters = ['%' + where + '%', '%' + where + '%','%' + where + '%']
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.livro WHERE Autor LIKE ? OR Titulo LIKE ? OR ISBN LIKE ?', parameters)
            else:
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.livro')
            data = result.fetchall()
            print(data)
            self.tableLivro.setColumnCount(6)
            self.tableLivro.setColumnWidth(0, 100)        
            self.tableLivro.setColumnWidth(1, 100)
            self.tableLivro.setColumnWidth(2, 100)
            self.tableLivro.setColumnWidth(3, 100)
            self.tableLivro.setColumnWidth(4, 100)
            self.tableLivro.setColumnWidth(5, 100)
            self.tableLivro.setRowCount(len(data))

            index = 0

            for row in data:
                self.tableLivro.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.tableLivro.setItem(index, 1, QTableWidgetItem(str(row[1])))
                self.tableLivro.setItem(index, 2, QTableWidgetItem(str(row[2])))
                self.tableLivro.setItem(index, 3, QTableWidgetItem(str(row[3])))
                self.tableLivro.setItem(index, 4, QTableWidgetItem(str(row[4])))
                self.tableLivro.setItem(index, 5, QTableWidgetItem(str(row[5])))
                index = index + 1

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Livros")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()      
    
        
if __name__ == '__main__':
    database = Database()
    application = QApplication(sys.argv) 
    view = MainWindow()
    view.show()
    application.exec()  