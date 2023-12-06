# Generador de Código - Analizador Semántico

Este generador de código está diseñado para agregar funcionalidades de análisis semántico a un código fuente previamente analizado léxica y sintácticamente. El objetivo es realizar verificaciones semánticas sobre las variables y las operaciones del código.

## Uso

1. **Preparación del Código Fuente:**
   - Asegúrate de tener un código fuente que ya haya pasado por el análisis léxico y sintáctico.
   - El análisis léxico y sintáctico debe producir una lista llamada `elementos` que contenga información sobre los tokens y lexemas del código.

2. **Integración del Generador de Código:**
   - Copia el código del generador y pégalo en tu script o programa Python en el lugar donde deseas realizar el análisis semántico.
   - Asegúrate de tener acceso a la lista `elementos` que contiene información sobre los tokens y lexemas generados en el análisis léxico y sintáctico.

3. **Ejecución del Generador:**
   - Sustituye la variable `codigo_fuente` con la variable que contiene la información del código original. Asegúrate de tener la lista `elementos` disponible.
   - Ejecuta el script y observa la salida en la consola. Verás tanto el código original como el código optimizado con las verificaciones semánticas.

4. **Resultados:**
   - El generador proporcionará mensajes de error semántico en caso de encontrar situaciones como el uso de variables no asignadas o la realización de operaciones con tipos de datos no válidos.
