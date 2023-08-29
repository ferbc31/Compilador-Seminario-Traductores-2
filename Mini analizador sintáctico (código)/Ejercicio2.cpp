#include <iostream>
#include <stack>
#include <string>

// Tabla LR(1)
int tabla[5][4] = {
    {2, 0, 0, 1},
    {0, 0, -1, 0},
    {0, 3, -3, 0},
    {2, 0, 0, 4},
    {0, 0, -2, 0}
};

// Identificadores y longitudes de reglas
int idReglas[2] = { 2, 2 };
int lonReglas[2] = { 3, 0 };

int getToken(const std::string& input, int& i) {
  if (i < input.size() && isalpha(input[i])) {
    while (i < input.size() && (isalpha(input[i]) || isdigit(input[i]))) {
      i++;
    }
    return 0;
  } else if (i < input.size() && input[i] == '+') {
    i++;
    return 1;
  } else if (i < input.size() && input[i] == '$') {
    i++;
    return 2;
  }
  return -1;
}

bool analizar(std::string input) {
  input += "$";
  std::stack<int> pila;
  pila.push(0);
  int i = 0;

  while (true) {
    int estado = pila.top();
    int token = getToken(input, i);
    int accion = tabla[estado][token];

    if (accion > 0) {
      pila.push(token);
      pila.push(accion);
    } else if (accion < 0) {
      int regla = -accion - 1;
      int numEliminar = lonReglas[regla];
      for (int j = 0; j < numEliminar; j++) {
        pila.pop();
      }
      pila.push(idReglas[regla]);
      pila.push(tabla[estado][idReglas[regla]]);
    } else if (accion == 0 && token == 2) {
      return true;
    } else {
      return false;
    }
  }
  return false;
}

int main() {
  std::string input;
  std::cout << "Ingrese una expresión (ejemplo: a+b+c+d+e+f): ";
  std::cin >> input;

  if (analizar(input)) {
    std::cout << "Expresión válida.\n";
  } else {
    std::cout << "Expresión inválida.\n";
  }
  return 0;
}

