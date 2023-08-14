from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem
from tela.main_ui import Ui_mainWindow
import pyodbc
import sys

global database

class Database:

    def __init__(self):
        self.connection = pyodbc.connect(driver = 'SQL Server', server = 'regulus.cotuca.unicamp.br', database = '', uid = '', pwd = '')
        print("entrou no banco de dados!")     

class MainWindow(QMainWindow, Ui_mainWindow):
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
        self.buttonDevolucao.clicked.connect(self.checked)
        self.buttonDevolucaoNao.clicked.connect(self.notChecked)


    def disable(self):

        self.textNumeroEmprestimo.setEnabled(not self.textNumeroEmprestimo.isEnabled())
        self.textNumeroLivro.setEnabled(not self.textNumeroLivro.isEnabled())
        self.textDevolvido.setEnabled(not self.textDevolvido.isEnabled())
        self.textNumeroBibliotecaria.setEnabled(not self.textNumeroBibliotecaria.isEnabled())
        self.textLocatario.setEnabled(not self.textLocatario.isEnabled())

    def clear(self):

        self.textNumeroEmprestimo.setText('')
        self.textNumeroLivro.setText('')
        self.textDevolvido.setText('')
        self.textNumeroBibliotecaria.setText('')
        self.textLocatario.setText('')


    def delete(self):

        codigo_emprestimo = self.tableEmprestimo.item(self.tableEmprestimo.currentRow(), 0).text()
        message = QMessageBox(self)
        message.setWindowTitle("Administrar Livro")
        message.setText("Você gostaria de excluir o Livro {}?".format(codigo_emprestimo))
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.setIcon(QMessageBox.Warning)
        button = message.exec_()

        if button == QMessageBox.Yes:
            try:
                database.connection.cursor().execute('DELETE FROM biblioteca.Emprestimo WHERE NumeroLivro = ?', codigo_emprestimo)
                database.connection.commit()
                self.list()
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao dos Emprestimos")
                message.setText('O Emprestimo {} foi excluído com sucesso!'.format(codigo_emprestimo))
                message.setIcon(QMessageBox.Information)
                message.exec()

            except Exception as error:
                message = QMessageBox(self)
                message.setWindowTitle("Sistema de Administracao dos Emprestimos")
                message.setText(error.args[0])
                message.setIcon(QMessageBox.Critical)
                message.exec()

    def search(self):

        self.list(self.textPesquisar.text()) 

    def new(self):

        self.disable()

    def save(self): 

        try:
            database.connection.cursor().execute('INSERT INTO biblioteca.Emprestimo VALUES (?,?,?,?)',  self.textDevolvido.text(), self.textNumeroLivro.text(), self.textNumeroBibliotecaria.text(),self.textLocatario.text())
            database.connection.cursor().commit()
            self.list()
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Emprestimos")
            message.setText('O Emrpestimo {} - {} foi incluído com sucesso!'.format(self.textNumeroEmprestimo.text()))
            message.setIcon(QMessageBox.Information)
            message.exec()
            self.disable()
            self.clear() 

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Emprestimos")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()  

    def cancel(self):

        self.disable()
        self.clear()
    
    def checked(self):
        try:
            codigo_emprestimo = self.tableEmprestimo.item(self.tableEmprestimo.currentRow(), 0).text()
            devolucao = "SIM"
            database.connection.cursor().execute("UPDATE biblioteca.Emprestimo SET devolucaoStatus = ? WHERE numeroEmprestimo LiKE ?", devolucao, codigo_emprestimo)
            database.connection.cursor().commit()
            self.list()
        
    
        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Emprestimos")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()  
    
    def notChecked(self):
        try:
            codigo_emprestimo = self.tableEmprestimo.item(self.tableEmprestimo.currentRow(), 0).text()
            devolucao = "NAO"
            database.connection.cursor().execute("UPDATE biblioteca.Emprestimo SET devolucaoStatus = ? WHERE numeroEmprestimo LiKE ?", devolucao, codigo_emprestimo)
            database.connection.cursor().commit()
            self.list()
        
        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Emprestimos")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()  

    def list(self, where = None):

        try:
            if where:
                parameters = ['%' + where + '%', '%' + where + '%','%' + where + '%', '%' + where + '%']
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.Emprestimo WHERE numeroEmprestimo LIKE ? OR numeroLivro LIKE ? OR numeroBibliotecario LIKE ? OR registroLocatario LIKE ?', parameters)
            else:
                result = database.connection.cursor().execute('SELECT * FROM biblioteca.Emprestimo')
            data = result.fetchall()

            self.tableEmprestimo.setColumnCount(5)
            self.tableEmprestimo.setColumnWidth(0, 100)        
            self.tableEmprestimo.setColumnWidth(1, 100)
            self.tableEmprestimo.setColumnWidth(2, 100)
            self.tableEmprestimo.setColumnWidth(3, 100)
            self.tableEmprestimo.setColumnWidth(4, 100)
            self.tableEmprestimo.setRowCount(len(data))

            index = 0

            for row in data:          
                self.tableEmprestimo.setItem(index, 0, QTableWidgetItem(str(row[0])))
                self.tableEmprestimo.setItem(index, 1, QTableWidgetItem(str(row[1])))
                self.tableEmprestimo.setItem(index, 2, QTableWidgetItem(str(row[2])))
                self.tableEmprestimo.setItem(index, 3, QTableWidgetItem(str(row[3])))
                self.tableEmprestimo.setItem(index, 4, QTableWidgetItem(str(row[4])))
                index = index + 1

        except Exception as error:
            message = QMessageBox(self)
            message.setWindowTitle("Sistema de Administracao dos Emprestimos")
            message.setText(error.args[0])
            message.setIcon(QMessageBox.Critical)
            message.exec()      
    
        
if __name__ == '__main__':
    database = Database()
    application = QApplication(sys.argv) 
    view = MainWindow()
    view.show()
    application.exec()  