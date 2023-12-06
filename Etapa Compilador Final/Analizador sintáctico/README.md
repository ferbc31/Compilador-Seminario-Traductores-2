## Analizador Léxico 

El analizador léxico se encarga de reconocer y clasificar los elementos presentes en una cadena de entrada. En este caso, la cadena de entrada es proporcionada a través de una interfaz gráfica construida con PyQt5. 🖥️

### Funcionamiento ⚙️

1. **Interfaz Gráfica:** La interfaz gráfica se compone de una ventana principal (`MainWindow`) que incluye elementos como campos de texto, botones y una tabla para mostrar los resultados. 📊

2. **Código del Analizador Léxico:** La función `analizador` se ejecuta al hacer clic en el botón "Enter". Esta función realiza los siguientes pasos:

   - Lee el texto ingresado en el campo de texto (`textEdit`).
   - Inicializa variables y prepara la cadena de entrada para el análisis.
   - Utiliza un bucle para recorrer la cadena e identificar tokens como identificadores, operadores, constantes, etc.
   - Almacena la información de cada elemento (lexema, token, id) en una lista llamada `elementos`.
   - Lee matrices y reglas desde archivos externos (`table.txt` y `rules.txt`).
   - Utiliza estas matrices y reglas para realizar un análisis sintáctico y determinar si la cadena es válida.
   - Muestra los resultados en la tabla de la interfaz gráfica.

3. **Resultados en la Tabla:** Los resultados del análisis léxico se presentan en la tabla de la interfaz gráfica. Cada fila de la tabla representa un elemento encontrado en la cadena, con columnas para el id, lexema y token correspondientes. 📑
<img width="351" alt="image" src="https://github.com/ferbc31/Compilador-Seminario-Traductores-2/assets/125149035/1051b508-cc57-48b0-9232-2d8a2f525f35">

4. **Análisis Sintáctico:** Si la cadena es válida desde el punto de vista léxico, el código realiza un análisis sintáctico adicional. Se detectan expresiones entre paréntesis, se crea un árbol de expresiones y se muestra en la consola la estructura de la expresión. 🌳

### Explicación Adicional 🗒️

- **Expresiones Entre Paréntesis:** El código identifica expresiones entre paréntesis y las reemplaza por letras mayúsculas en la cadena original. Luego, realiza un análisis sintáctico de estas expresiones.

- **Árbol de Expresiones:** Se construye un árbol de expresiones que representa la estructura jerárquica de la cadena analizada. El árbol se muestra en la consola con información sobre los signos y las subexpresiones. 🌐

El código incluye comentarios que proporcionan detalles adicionales sobre el proceso de análisis léxico y sintáctico. 📝
