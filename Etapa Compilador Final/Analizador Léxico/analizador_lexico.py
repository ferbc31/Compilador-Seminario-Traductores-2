from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os

#Todo esto es para la interfaz grafica
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 240, 621, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 30, 200, 100))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(470, 30, 200, 100))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        ###########################################################
        self.pushButton.clicked.connect(self.analizador)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analizador léxico"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
    
    def analizador(self):
        texto = self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(texto)
        
        os.system('cls')
        elementos=[]
        estado=0
        indice=0
        id= 0
        cadena=texto+'$'
        while(indice<=(len(cadena)-1)  and estado==0):  
                lexema=''
                token='error'
                while(indice<=(len(cadena)-1) and estado!=20):
                    if estado==0:
                        if cadena[indice].isspace():
                            estado=0
                        elif cadena[indice].isalpha():
                            estado = 1
                            token='id'
                            id=1
                            lexema += cadena[indice]
                        elif cadena[indice]=='$':
                            estado=20
                            lexema+=cadena[indice]
                            token='pesos'
                            id=18
                        elif cadena[indice]=='=':
                            lexema+=cadena[indice]
                            token='asignacion'
                            estado=20
                            id=8
                        elif cadena[indice]=='+':
                            lexema+=cadena[indice]
                            token='opSuma'
                            estado=20
                            id=14
                        elif cadena[indice]=='-':
                            lexema+=cadena[indice]
                            token='opResta'
                            estado=20
                            id=14
                        elif cadena[indice]=='*':
                            lexema+=cadena[indice]
                            token='opMul'
                            estado=20
                            id=16
                        elif cadena[indice]==';':
                            lexema+=cadena[indice]
                            token='puntoComa'
                            estado=20
                            id=2
                        elif cadena[indice]=='(':
                            lexema+=cadena[indice]
                            token='parentIzq'
                            estado=20
                            id=4
                        elif cadena[indice]==')':
                            lexema+=cadena[indice]
                            token='parentDere'
                            estado=20
                            id=5
                        elif cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='constante'
                            estado=2
                            id=13
                        elif cadena[indice] == '/':
                            lexema+=cadena[indice]
                            token='opDiv'
                            estado=20
                            id=15
      
                        else:
                            id='no'
                            estado=20
                            token='error'
                            lexema=cadena[indice]
                        indice+=1
                        
                    elif estado==1:
                        if cadena[indice].isalpha():
                            lexema+=cadena[indice]
                            token='id'
                            id=17
                            estado=1
                            indice+=1
                        elif cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='id'
                            id=17
                            estado=1
                            indice+=1
                        else:
                            estado=20
                    elif estado==2:
                        if cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='constante'
                            id=17
                            indice+=1
                            estado=2
                        elif cadena[indice] == ".":
                            lexema+=cadena[indice]
                            token='constante'
                            id=17
                            estado=3
                            indice+=1
                        else:
                            estado=20
                    elif estado==3:
                        if cadena[indice].isdigit():
                            lexema+=cadena[indice]
                            token='constante'
                            id=17
                            indice+=1
                            estado=3
                        else:
                            estado=20
                        
                estado=0
                elementos.append({'id':id,'token':token,'lexema':lexema})
                
            
            
        with open('tabla.txt', 'r') as file:
            doc = file.read()

        filas = doc.splitlines()
        matriz = []
        for fila in filas:
            ele = fila.split()
            fila_numeros = [int(num) for num in ele]
            matriz.append(fila_numeros)
        
        with open('reglas.txt', 'r') as file:
            doc = file.read()

        filas = doc.splitlines()
        reglas = []
        for fila in filas:
            ele = fila.split()
            fila_numeros = [int(num) for num in ele]
            reglas.append(fila_numeros)
        

        cad = []
        cad = elementos[::-1]
        pila = []
        pila.append(0)
        n = 0
        c = 0

        while(True):
            if(cad[len(cad)-1]['token']=='id'):
                n = 0
            if(cad[len(cad)-1]['token']=='asignacion'):
                n = 1
            if(cad[len(cad)-1]['token']=='opSuma'):
                n = 2
            if(cad[len(cad)-1]['token']=='opResta'):
                n = 3
            if(cad[len(cad)-1]['token']=='opMul'):
                n = 4
            if(cad[len(cad)-1]['token']=='opDiv'):
                n = 5
            if(cad[len(cad)-1]['token']=='parentIzq'):
                n = 6
            if(cad[len(cad)-1]['token']=='parentDere'):
                n = 7
            if(cad[len(cad)-1]['token']=='constante'):
                n = 8
            if(cad[len(cad)-1]['token']=='puntoComa'):
                n = 9
            if(cad[len(cad)-1]['token']=='pesos'):
                n = 10
        
        
            oper = matriz [pila[len(pila)-1]] [n+1]
            
            
            c+=1
            #print("----------------- PASO ",c, "---------------------")
            #print("Tabla: ", oper)
            cadenaValida = False
            
            if(oper == 0):
                print("Cadena Invalida :(")
                break

            if(oper == -1):
                print("Cadena Valida :)")
                cadenaValida = True
                break
            
            if(oper > 0):
                pila.append(cad[len(cad)-1]['token'])
                cad.pop()
                pila.append(oper)
                                
            if(oper < -1):
                for i in range((reglas[abs(oper)-1][1])*2):
                    pila.pop()
                
                row = pila[len(pila)-1]
                regla = reglas[abs(oper)-1][0]
                

                pila.append(regla)
                pila.append(matriz[row][regla+1])
                
        for r in range(len(elementos), self.tableWidget.rowCount()):
            self.tableWidget.removeRow(len(elementos))
        for r in range(len(elementos)):
            rowAct=self.tableWidget.rowCount()
            if rowAct<=r:
                self.tableWidget.insertRow(rowAct)
                id=str(elementos[r]['id'])
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(id))
                self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(elementos[r]['lexema']))
                self.tableWidget.setItem(r,2,QtWidgets.QTableWidgetItem(elementos[r]['token']))
            else:
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(id))
                self.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(elementos[r]['lexema']))
                self.tableWidget.setItem(r,2,QtWidgets.QTableWidgetItem(elementos[r]['token']))

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
