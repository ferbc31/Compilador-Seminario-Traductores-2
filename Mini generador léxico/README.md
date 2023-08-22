# MINI GENERADOR LÉXICO
El programa analiza una cadena de entrada para identificar y clasificar "tokens":

Tipos de Tokens:

  **IDENTIFICADOR**: Palabras compuestas solo por letras.

  **NUMERO_DECIMAL**: Secuencias numéricas que pueden contener un punto.

  **NO_DEFINIDO:** Cualquier otra secuencia que no se ajuste a las dos categorías anteriores.

***Análisis de caracteres:***

  **esCaracterValido** _verifica si un carácter es una letra._

  **esNumero** _verifica si un carácter es un dígito._

  **Descomposición** y **Mostrar**:
  
**descomponerTexto** _examina la cadena, caracter por caracter, agrupando los caracteres en tokens según su tipo.
Una vez identificado un token, mostrarToken imprime el token con su respectiva clasificación.


En la función **main**, se proporciona una cadena de prueba y se procede a descomponerla y mostrar los tokens identificados. Tokens inesperados o que no se ajusten a las categorías principales se etiquetan y se muestran como "NoValido"._
