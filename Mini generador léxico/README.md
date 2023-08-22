# MINI GENERADOR LÉXICO
Benavides Castro Fernando 2023B Materia SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJES II Seccion D02

El programa analiza léxicamente una cadena de entrada para identificar y
clasificar \"tokens\":

1.  **Tipos de Tokens**: Hay tres categorías:

    -   **IDENTIFICADOR**: Palabras compuestas solo por letras.

    -   **NUMERO_DECIMAL**: Secuencias numéricas que pueden contener un
        punto.

    -   **NO_DEFINIDO**: Cualquier otra secuencia que no se ajuste a las
        dos categorías anteriores.

2.  **Análisis de caracteres**:

    -   **esCaracterValido** verifica si un carácter es una letra.

    -   **esNumero** verifica si un carácter es un dígito.

3.  **Descomposición y Mostrar**:

    -   **descomponerTexto** examina la cadena, caracter por caracter,
        agrupando los caracteres en tokens según su tipo.

    -   Una vez identificado un token, **mostrarToken** imprime el token
        con su respectiva clasificación.

4.  En la función **main**, se proporciona una cadena de prueba y se
    procede a descomponerla y mostrar los tokens identificados. Tokens
    inesperados o que no se ajusten a las categorías principales se
    etiquetan y se muestran como \"NoValido\".
