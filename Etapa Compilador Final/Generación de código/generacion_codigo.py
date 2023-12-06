from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os

def generar_codigo_optimizado(codigo_fuente):

    variables_asignadas = set()
    tipos_de_datos = {'id': 'indefinido'} 
    cad = []  
    pila = []
    pila.append(0)
    n = 0
    c = 0

    while cad:
        if cad[-1]['token'] == 'id':
            n = 0
        elif cad[-1]['token'] == 'asignacion':
            n = 1
            id_actual = cad[-1]['lexema']
            if id_actual not in variables_asignadas:
                print(f"Error semántico: Variable '{id_actual}' utilizada antes de ser asignada.")
                return
        elif cad[-1]['token'] in {'opSuma', 'opResta', 'opMul', 'opDiv'}:
            n = 2
            tipo_izquierda = tipos_de_datos.get(cad[-3]['lexema'], 'indefinido')
            tipo_derecha = tipos_de_datos.get(cad[-1]['lexema'], 'indefinido')
            if tipo_izquierda != tipo_derecha or tipo_izquierda == 'indefinido':
                print("Error semántico: Operación con tipos de datos no válidos.")
                return

        oper = matriz[pila[-1]][n + 1]

        c += 1
        cadenaValida = False

        if oper == 0:
            print("Cadena Invalida :(")
            break
        if oper == -1:
            print("Cadena Valida :)")
            cadenaValida = True
            break
        if oper > 0:
            pila.append(cad[-1]['token'])
            cad.pop()
            pila.append(oper)
        if oper < -1:
            for i in range((reglas[abs(oper) - 1][1]) * 2):
                pila.pop()

            row = pila[-1]
            regla = reglas[abs(oper) - 1][0]

            pila.append(regla)
            pila.append(matriz[row][regla + 1])

    for r in range(len(elementos), self.tableWidget.rowCount()):
        self.tableWidget.removeRow(len(elementos))
    for r in range(len(elementos)):
        rowAct = self.tableWidget.rowCount()
        if rowAct <= r:
            self.tableWidget.insertRow(rowAct)
            id = str(elementos[r]['id'])
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(id))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(elementos[r]['lexema']))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(elementos[r]['token']))
            # Actualizar información de variables asignadas y tipos de datos
            if elementos[r]['token'] == 'id' and elementos[r + 1]['token'] == 'asignacion':
                variables_asignadas.add(elementos[r]['lexema'])
                tipo_dato = elementos[r + 2]['token']
                tipos_de_datos[elementos[r]['lexema']] = tipo_dato
        else:
            self.tableWidget.setItem(r, 0, QtWidgets.QTableWidgetItem(id))
            self.tableWidget.setItem(r, 1, QtWidgets.QTableWidgetItem(elementos[r]['lexema']))
            self.tableWidget.setItem(r, 2, QtWidgets.QTableWidgetItem(elementos[r]['token']))

# Ejemplo de código fuente
codigo_fuente_ejemplo = """
a = 5
b = 10
c = a + b
"""
generar_codigo_optimizado(codigo_fuente_ejemplo)
