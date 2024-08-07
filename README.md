# Convertidor de Archivos

Esta aplicación en Python permite la conversión entre formatos de archivos comunes: Excel, JSON y CSV. Desarrollada usando Tkinter para la interfaz gráfica y `pandas` para el procesamiento de datos, la aplicación proporciona una forma sencilla de convertir entre estos formatos.

## Requisitos

- Python 3.6 o superior
- Paquetes Python: `pandas`

## Instalación

1. **Clona el repositorio** o descarga el archivo Python.
2. **Instala las dependencias** usando pip:

    ```bash
    pip install pandas
    ```

## Uso

1. **Ejecuta la aplicación**. Puedes hacerlo ejecutando el archivo Python en tu terminal o desde un entorno de desarrollo:

    ```bash
    python main.py
    ```

2. **Interfaz de Usuario**:
   - **Excel a JSON**: Selecciona un archivo Excel para convertirlo a JSON. La aplicación guardará el archivo JSON resultante en la ubicación que elijas.
   - **JSON a Excel**: Selecciona un archivo JSON para convertirlo a Excel. La aplicación guardará el archivo Excel resultante en la ubicación que elijas.
   - **CSV a Excel**: Selecciona un archivo CSV para convertirlo a Excel. La aplicación guardará el archivo Excel resultante en la ubicación que elijas.
   - **Excel a CSV**: Selecciona un archivo Excel para convertirlo a CSV. La aplicación guardará el archivo CSV resultante en la ubicación que elijas.
   - **CSV a JSON**: Selecciona un archivo CSV para convertirlo a JSON. La aplicación guardará el archivo JSON resultante en la ubicación que elijas.
   - **JSON a CSV**: Selecciona un archivo JSON para convertirlo a CSV. La aplicación guardará el archivo CSV resultante en la ubicación que elijas.

3. **Registro de Actividades**: La aplicación mantiene un registro de las conversiones realizadas en el área de texto de la interfaz, proporcionando información sobre los archivos convertidos y cualquier error que pueda haber ocurrido.

## Ejemplo de Uso

1. **Convertir Excel a JSON**:
   - Haz clic en "Excel a JSON".
   - Selecciona el archivo Excel que deseas convertir.
   - Elige la ubicación para guardar el archivo JSON.

2. **Convertir JSON a Excel**:
   - Haz clic en "JSON a Excel".
   - Selecciona el archivo JSON que deseas convertir.
   - Elige la ubicación para guardar el archivo Excel.

3. **Ver registro de actividades**:
   - Observa el área de texto para revisar las conversiones realizadas y cualquier mensaje de error.
