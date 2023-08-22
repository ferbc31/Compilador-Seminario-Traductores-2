/*
Nombre: Benavides Castro Fernando
Materia: SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJES II
Sección: D02
Calendario: 2023B
Profesor: MICHEL EMANUEL LOPEZ FRANCO
*/
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

namespace Lexico {
    enum TipoToken {
        IDENTIFICADOR,
        NUMERO_DECIMAL,
        OPERADOR_ADICION,
        OPERADOR_MULTIPLICACION,
        OPERADOR_ASIGNACION,
        OPERADOR_RELACIONAL,
        OPERADOR_AND,
        OPERADOR_OR,
        OPERADOR_NOT,
        PARENTESIS,
        LLAVE,
        PUNTO_Y_COMA,
        PALABRA_RESERVADA,
        NO_DEFINIDO
    };

    unordered_set<string> palabrasReservadas = {"if", "while", "return", "else", "int", "float"};

    bool esCaracterValido(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }

    bool esNumero(char c) {
        return c >= '0' && c <= '9';
    }

    void mostrarToken(const string& token, TipoToken tipo) {
        if (!token.empty()) {
            switch (tipo) {
                case IDENTIFICADOR: cout << "Identificador: " << token << endl; break;
                case NUMERO_DECIMAL: cout << "Numero: " << token << endl; break;
                case OPERADOR_ADICION: cout << "Operador de adicion: " << token << endl; break;
                case OPERADOR_MULTIPLICACION: cout << "Operador de multiplicacion: " << token << endl; break;
                case OPERADOR_ASIGNACION: cout << "Operador de asignacion: " << token << endl; break;
                case OPERADOR_RELACIONAL: cout << "Operador relacional: " << token << endl; break;
                case OPERADOR_AND: cout << "Operador AND: " << token << endl; break;
                case OPERADOR_OR: cout << "Operador OR: " << token << endl; break;
                case OPERADOR_NOT: cout << "Operador NOT: " << token << endl; break;
                case PARENTESIS: cout << "Parentesis: " << token << endl; break;
                case LLAVE: cout << "Llave: " << token << endl; break;
                case PUNTO_Y_COMA: cout << "Punto y coma: " << token << endl; break;
                case PALABRA_RESERVADA: cout << "Palabra reservada: " << token << endl; break;
                case NO_DEFINIDO: cout << "NoValido: " << token << endl; break;
            }
        }
    }

    // Función que descompone el texto en tokens
    void descomponerTexto(const string& entrada) {
        string token;
        TipoToken tipoActual = NO_DEFINIDO;

        for (size_t i = 0; i < entrada.size(); i++) {
            char caracter = entrada[i];
            if (esCaracterValido(caracter) || (caracter == '_' && tipoActual == IDENTIFICADOR)) {
                token += caracter;
                tipoActual = IDENTIFICADOR;
            } else if (esNumero(caracter)) {
                token += caracter;
                tipoActual = NUMERO_DECIMAL;
            } else {
                if (!token.empty() && palabrasReservadas.find(token) != palabrasReservadas.end()) {
                    tipoActual = PALABRA_RESERVADA;
                }
                mostrarToken(token, tipoActual);
                token = "";

                if (caracter == '+' || caracter == '-') {
                    token = caracter;
                    tipoActual = OPERADOR_ADICION;
                } else if (caracter == '*' || caracter == '/') {
                    token = caracter;
                    tipoActual = OPERADOR_MULTIPLICACION;
                } else if (caracter == '=') {
                    if (i + 1 < entrada.size() && entrada[i + 1] == '=') {
                        token = caracter;
                        token += entrada[++i];
                        tipoActual = OPERADOR_RELACIONAL;
                    } else {
                        token = caracter;
                        tipoActual = OPERADOR_ASIGNACION;
                    }
                } else if (caracter == '<' || caracter == '>' || caracter == '!') {
                    token = caracter;
                    if (i + 1 < entrada.size() && (entrada[i + 1] == '=' || (caracter == '!' && entrada[i + 1] == '='))) {
                        token += entrada[++i];
                    }
                    tipoActual = OPERADOR_RELACIONAL;
                } else if (caracter == '&' && i + 1 < entrada.size() && entrada[i + 1] == '&') {
                    token = caracter;
                    token += entrada[++i];
                    tipoActual = OPERADOR_AND;
                } else if (caracter == '|' && i + 1 < entrada.size() && entrada[i + 1] == '|') {
                    token = caracter;
                    token += entrada[++i];
                    tipoActual = OPERADOR_OR;
                } else if (caracter == '!') {
                    token = caracter;
                    tipoActual = OPERADOR_NOT;
                } else if (caracter == '(' || caracter == ')') {
                    token = caracter;
                    tipoActual = PARENTESIS;
                } else if (caracter == '{' || caracter == '}') {
                    token = caracter;
                    tipoActual = LLAVE;
                } else if (caracter == ';') {
                    token = caracter;
                    tipoActual = PUNTO_Y_COMA;
                } else {
                    token = caracter;
                    tipoActual = NO_DEFINIDO;
                }
                mostrarToken(token, tipoActual);
                token = "";
            }
        }
    }
}

int main() {
    string contenido = "1+a1*-><;=&&||!(){}";
    cout << "Procesando contenido:" << endl;
    Lexico::descomponerTexto(contenido);

    return 0;
}
