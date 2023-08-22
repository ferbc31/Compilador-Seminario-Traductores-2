/*
Nombre: Benavides Castro Fernando
Materia: SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJES II
Sección: D02
Calendario: 2023B
Profesor: MICHEL EMANUEL LOPEZ FRANCO
*/

#include <iostream>
#include <string>

using namespace std;

namespace Lexico {
    enum TipoToken {
        IDENTIFICADOR,
        NUMERO_DECIMAL,
        NO_DEFINIDO
    };

    bool esCaracterValido(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }

    bool esNumero(char c) {
        return c >= '0' && c <= '9';
    }

    void mostrarToken(const string& token, TipoToken tipo) {
        if (!token.empty()) {
            switch (tipo) {
                case NUMERO_DECIMAL:
                    cout << "Numero decimal: " << token << endl;
                    break;
                case IDENTIFICADOR:
                    cout << "Identificador: " << token << endl;
                    break;
                case NO_DEFINIDO:
                    cout << "NoValido: " << token << endl;
                    break;
            }
        }
    }

    // Función que descompone el texto en tokens
    void descomponerTexto(const string& entrada) {
        string token;
        TipoToken tipoActual = NO_DEFINIDO;

        for (char caracter : entrada) {
            if (esCaracterValido(caracter)) {
                if (tipoActual == NO_DEFINIDO) {
                    mostrarToken(token, tipoActual);
                    token = "";
                }
                token += caracter;
                tipoActual = IDENTIFICADOR;
            } else if (esNumero(caracter)) {
                if (tipoActual == NO_DEFINIDO) {
                    mostrarToken(token, tipoActual);
                    token = "";
                }
                token += caracter;
                if (tipoActual != IDENTIFICADOR) tipoActual = NUMERO_DECIMAL;
            } else if (caracter == '.' && tipoActual == NUMERO_DECIMAL) {
                token += caracter;
            } else if (caracter != ' ' && tipoActual != IDENTIFICADOR && tipoActual != NUMERO_DECIMAL) {
                token += caracter;
                tipoActual = NO_DEFINIDO;
            } else {
                mostrarToken(token, tipoActual);
                token = "";
                tipoActual = NO_DEFINIDO;
            }
        }
        if (!token.empty()) {
            mostrarToken(token, tipoActual);
        }
    }
}

int main() {
    string contenido = "1 2 3 a b c a1 a2 a3 * +";
    cout << "Procesando contenido:" << endl;
    Lexico::descomponerTexto(contenido);

    return 0;
}
