/*
Nombre: Benavides Castro Fernando
Materia: SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJES II
Sección: D02
Calendario: 2023B
Profesor: MICHEL EMANUEL LOPEZ FRANCO
*/

#include <iostream>
#include <stack>
#include <string>

// Tabla LR(1)
int tabla[5][4] = {
    {2, 0, 0, 1},
    {0, 0, -1, 0},
    {0, 3, 0, 0},
    {4, 0, 0, 0},
    {0, 0, -2, 0}
};

// Función para obtener el token de una entrada y también devolver el identificador detectado
int getToken(const std::string& input, int& i, std::string& detectedId) {
    detectedId = "";
    if (i < input.size() && isalpha(input[i])) { // Si es una letra
        while (i < input.size() && (isalpha(input[i]) || isdigit(input[i]))) {
            detectedId += input[i];
            i++;
        }
        return 0; // identificador
    } else if (i < input.size() && input[i] == '+') {
        i++;
        return 1; // +
    } else if (i < input.size() && input[i] == '$') {
        i++;
        return 2; // pesos
    }
    return -1; // token inválido
}

bool analizar(std::string input) {
    input += "$";
    std::stack<int> pila;
    pila.push(0);
    int i = 0;

    while (i < input.size()) {
        int estado = pila.top();
        std::string detectedId;
        int token = getToken(input, i, detectedId);
        int accion = tabla[estado][token];

        if (accion > 0) {
            pila.push(token);
            pila.push(accion);
        } else if (accion < 0) {
            int regla = -accion;
            if (regla == 1) {
                for (int j = 0; j < 3; j++) {
                    pila.pop();
                }
            } else if (regla == 2) {
                pila.pop();
            }
            estado = pila.top();
            pila.push(tabla[estado][3]);
        } else if (accion == 0 && token == 2) {
            return true;
        } else {
            return false;
        }
    }
    return true;
}

int main() {
    std::string input;
    std::cout << "Ingrese una expresión (ejemplo: hola+mundo): ";
    std::cin >> input;

    if (analizar(input)) {
        std::cout << "Expresión valida.\n";
    } else {
        std::cout << "Expresión invalida.\n";
    }
    return 0;
}
