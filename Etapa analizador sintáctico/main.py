class Lexico:
    def __init__(self, cadena):
        self.cadena = cadena
        self.tokens = []
        self.analizar()

    def analizar(self):
        for caracter in self.cadena:
            if caracter.isalpha():  
                self.tokens.append(0)  # Identificador
            elif caracter == '+':
                self.tokens.append(1)  # +
            else:
                print(f"Caracter no reconocido: {caracter}")
                return  # Si se encuentra un carácter no reconocido, se detiene el análisis.
        self.tokens.append(2)  # Añadir el símbolo de peso al final

class AnalizadorLR:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = [0]
        self.tabla_LR = [
            [2, 0, 0, 1],
            [0, 0, -1, 0],
            [0, 3, -3, 0],
            [2, 0, 0, 4],
            [0, 0, -2, 0]
        ]

    def analizar(self):
        entrada = self.tokens.copy()
        while entrada:
            accion = self.tabla_LR[self.stack[-1]][entrada[0]]

            # Desplazamiento
            if accion > 0:
                self.stack.append(accion)
                entrada.pop(0)

            # Reducción
            elif accion < 0:
                regla = abs(accion) - 1  # Convertir la acción en índice y ajustar
                for _ in range(idReglas[regla]):
                    self.stack.pop()
                # Mover al estado correspondiente después de la reducción
                self.stack.append(self.tabla_LR[self.stack[-1]][3])

            # Aceptado o Error
            else:
                if entrada[0] == 2:  # Si el símbolo de peso es el siguiente, es aceptado
                    return True
                else:
                    return False  # Entrada inválida

        return False

if __name__ == "__main":
    cadena = "a+a+a"
    lexico = Lexico(cadena)
    analizador = AnalizadorLR(lexico.tokens)
    if analizador.analizar():
        print(f"La cadena '{cadena}' es válida.")
    else:
        print(f"La cadena '{cadena}' no es válida.")
