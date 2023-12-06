# Analizador Sintáctico
Este código implementa un analizador léxico y sintáctico para un lenguaje de expresiones matemáticas sencillas. A continuación, se proporciona información sobre la implementación del analizador sintáctico en el código proporcionado.

### Estructura del Código

1. **Importación de Módulos:**
   - El código comienza importando los módulos necesarios de PyQt5 y otros módulos estándar de Python.

2. **Clase Ui_MainWindow:**
   - La clase `Ui_MainWindow` define la interfaz gráfica de la aplicación utilizando PyQt5.
   - Contiene widgets como botones, cuadros de texto y una tabla para mostrar resultados.
   - La función `analizador` se conecta al botón y realiza el análisis sintáctico de la entrada.

3. **Método analizador:**
   - Este método realiza el análisis sintáctico de la cadena de entrada.
   - Utiliza una tabla de análisis sintáctico y reglas de producción para validar la cadena.
   - Si la cadena es válida, se realiza un análisis adicional para identificar y mostrar las expresiones entre paréntesis.
   - Finalmente, se construye y muestra un árbol sintáctico en la consola.

4. **Funciones Auxiliares:**
   - `encontrar_expresiones_entre_parentesis`: Busca y devuelve expresiones entre paréntesis en la cadena.
   - `mulDiv` y `sumRest`: Funciones recursivas que construyen y muestran el árbol sintáctico.

5. **Uso de PyQt5:**
   - Se utiliza PyQt5 para la interfaz gráfica, conectando la función `analizador` al clic del botón.

6. **Resultados en la Tabla:**
   - Los resultados del análisis se muestran en una tabla en la interfaz gráfica.

### Ejecución del Programa

- Si se ejecuta este script directamente, se creará una interfaz gráfica que permite al usuario ingresar una cadena.
- Después de hacer clic en el botón "Enter", se realiza el análisis sintáctico y los resultados se muestran en la tabla.

### Requisitos

- PyQt5 debe estar instalado para la ejecución correcta de la interfaz gráfica.

### Archivos Adicionales

- El código hace referencia a dos archivos externos: `tabla.txt` y `reglas.txt`, que contienen la tabla de análisis y las reglas de producción respectivamente.

### Observaciones

- El código asume que la cadena de entrada es una expresión matemática válida en el lenguaje definido.
- Se recomienda tener los archivos `tabla.txt` y `reglas.txt` en el mismo directorio que este script para un funcionamiento adecuado.

## Funcionamiento del Analizador Sintáctico
Al hacer clic en el botón "Enter", se activa la función `analizador`, que realiza la verificación sintáctica de la expresión ingresada. El código del analizador sintáctico está diseñado para reconocer elementos como identificadores, operadores y constantes.

El análisis sintáctico utiliza una tabla y reglas predefinidas para determinar si la expresión es válida. Los resultados se muestran en la tabla de la interfaz gráfica.

<img width="345" alt="image" src="https://github.com/ferbc31/Compilador-Seminario-Traductores-2/assets/125149035/c168fa86-948c-4885-b114-ab08911838b7">
<img width="223" alt="image" src="https://github.com/ferbc31/Compilador-Seminario-Traductores-2/assets/125149035/a4e0d25f-b1f2-4fa6-b3a8-9a0ad3b37213">


