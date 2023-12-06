# Analizador Semántico

Este componente se encarga de verificar algunas restricciones semánticas básicas durante el análisis de un código fuente. Vamos a entender las principales funcionalidades de este analizador:

1. **Uso de Variables**
   - **Objetivo:** Garantizar que las variables se utilicen después de ser asignadas.
   - **Implementación:** Detecta si una variable se está utilizando antes de haber sido asignada, evitando así errores de referencia .

2. **Tipos de Datos**
   - **Objetivo:** Verificar que las operaciones se realicen solo con tipos de datos válidos.
   - **Implementación:** Identifica y maneja errores semánticos relacionados con operaciones entre tipos de datos incompatibles.

## Uso del Analizador 🚀

El analizador semántico está integrado en un programa más amplio que incluye análisis léxico y sintáctico. Simplemente ejecuta el programa y proporciona el código fuente para obtener mensajes de error semántico si se violan las reglas mencionadas.
