# Escribimos en el README.md
%%writefile README.md

- Elías García Infante

- Organización Empresarial - UTN TUP

Escenario B - Análisis de Ventas de una Pequeña Empresa

Este Trabajo Practico fue desarrollado utilizando las siguientes herramientas:
- Git
- GitHub
- Jira
- google colab
- Python

El objetivo del trabajo es analizar los datos de ventas de una empresa para obtener información sobre el desempeño de la misma.

El programa permite:
- Leer un archivo CSV con datos de ventas de una empresa
- Calcular ventas totales de una empresa
- Identificar el producto más vendido de una empresa
- Generar un gráfico de ventas

La estructura del repositorio es la siguiente:
- datos/: contiene el archivo CSV
- scripts/: contiene el programa principal
- resultados/: contiene el gráfico y la informacion obtenida del programa

Como ejecutar el programa:
1. Abrir Google Colab
2. Clonar el repositorio
3. Ejecutar el archivo: python scripts/analisis_de_ventas.py
4. Revisar los resultados generados en la carpeta resultados/

Buenas practicas implementadas:
- Uso de .gitignore para excluir archivos y carpetas innecesarias
- Trazabilidad de Commit: Los commits empiezan con el ID del issue de Jira correspondiente
- Reproducibilidad: El codigo se ejecuta correctamente en google Colab
- Calidad de Código: Incluye comentarios técnicos que expliquen el por qué de la lógica implementada
- Protección de Credenciales: No se expone el Token en celdas visibles ni en el repositorio
