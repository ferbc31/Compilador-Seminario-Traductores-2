## Clase Lexico:

La clase Lexico se encarga de realizar el análisis léxico de la cadena de entrada. Esto significa que toma la cadena de caracteres y la divide en "tokens", que son unidades léxicas o símbolos reconocidos en el lenguaje. En este caso, la gramática es bastante simple y reconoce identificadores (formados por letras) y el símbolo '+'.

- `__init__(self, cadena)`: El constructor recibe la cadena de entrada como argumento.

- `analizar(self)`: Este método realiza el análisis léxico. Recorre cada carácter de la cadena de entrada y clasifica cada carácter en un token. En este caso, se clasifican las letras como identificadores (token 0) y el símbolo '+' como un token 1. Si se encuentra un carácter no reconocido, se imprime un mensaje de error.

## Clase AnalizadorLR:

La clase AnalizadorLR es un analizador sintáctico que utiliza una tabla de análisis LR(1) para determinar si la cadena cumple con la gramática especificada. La tabla de análisis LR(1) es una herramienta comúnmente utilizada en el análisis sintáctico de compiladores.

- `__init__(self, tokens)`: El constructor recibe los tokens generados por la clase Lexico.

- `analizar(self)`: Este método realiza el análisis sintáctico utilizando la tabla de análisis LR(1). La tabla define las acciones a tomar en función del estado actual del analizador y el token de entrada. Las acciones pueden ser "Shift" (desplazar), "Reduce" (reducir) o "Aceptar" (indicando que la cadena es válida). En caso de no encontrar una acción válida, se considera un error.

### El proceso de análisis funciona de la siguiente manera:

1. Se crea una copia de la lista de tokens generada por Lexico.

2. Se inicia un bucle mientras haya tokens en la lista de entrada.

3. Se consulta la tabla de análisis LR(1) para determinar la acción a tomar en función del estado actual y el token de entrada.

4. Si la acción es "Shift," se mueve el token de entrada a la pila y se desplaza al siguiente estado.

5. Si la acción es "Reduce," se aplica una regla de reducción. Las reglas de reducción están definidas en la tabla y se utilizan para simplificar la pila y avanzar al siguiente estado.

6. Si la acción es "Aceptar," se considera que la cadena es válida.

7. Si no se encuentra una acción válida en la tabla, se considera un error y se retorna False.

El código proporcionado ejecuta estas operaciones y, al final, imprime si la cadena de entrada es válida o no.

