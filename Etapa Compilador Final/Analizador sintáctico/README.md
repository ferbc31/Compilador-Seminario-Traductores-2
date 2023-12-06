# Analizador Sintáctico con Interfaz Gráfica en PyQt5

Este proyecto implementa un analizador sintáctico con interfaz gráfica utilizando la biblioteca PyQt5 en Python. El analizador sintáctico verifica la validez de expresiones ingresadas y muestra los resultados en una tabla.

## Requisitos Previos
Asegúrate de tener Python instalado en tu computadora. Además, se requiere la instalación de la biblioteca PyQt5. Puedes instalarla ejecutando el siguiente comando:

```bash
pip install PyQt5
```

## Interfaz Gráfica
La interfaz gráfica se crea con PyQt5 y consta de una ventana principal que incluye:

- Un campo de texto (`QTextEdit`) para ingresar la expresión.
- Un botón (`QPushButton`) para ejecutar el analizador.
- Una tabla (`QTableWidget`) para mostrar los resultados.

La ventana se inicializa con la función `setupUi`, donde se definen los elementos y su disposición en la interfaz.

```python
# ...

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Configuración de la interfaz gráfica
        # ...

    def retranslateUi(self, MainWindow):
        # Traducciones de la interfaz gráfica
        # ...

    def analizador(self):
        # Lógica del analizador sintáctico
        # ...
```

## Funcionamiento del Analizador Sintáctico
Al hacer clic en el botón "Enter", se activa la función `analizador`, que realiza la verificación sintáctica de la expresión ingresada. El código del analizador sintáctico está diseñado para reconocer elementos como identificadores, operadores y constantes.

El análisis sintáctico utiliza una tabla y reglas predefinidas para determinar si la expresión es válida. Los resultados se muestran en la tabla de la interfaz gráfica.

<img width="345" alt="image" src="https://github.com/ferbc31/Compilador-Seminario-Traductores-2/assets/125149035/c168fa86-948c-4885-b114-ab08911838b7">

## Cómo Ejecutar el Proyecto
1. Asegúrate de tener Python instalado.
2. Instala PyQt5 utilizando `pip install PyQt5`.
3. Ejecuta el script con el código proporcionado.

```bash
python nombre_del_script.py
```
