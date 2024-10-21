# **Documentación Rápida**

## **Descripción General**
Este script utiliza la API de **Google Generative AI** para interactuar con el modelo **Gemini 1.5** y generar diferentes tipos de contenido. El programa ofrece las siguientes funcionalidades:
1. Generación de texto a partir de una entrada dada.
2. Generación de contenido desde una imagen y un texto de descripción.
3. Generación de código a partir de una descripción.
4. Conversación con el modelo, donde las interacciones se almacenan y se guardan en un archivo `.md` al final de la sesión.
5. Un menú interactivo que permite al usuario seleccionar entre las distintas opciones.

---

## **Instalación**

Para instalar la biblioteca de **Google Generative AI**, puedes ejecutar el siguiente comando:

```bash
pip install -q -U google-generativeai
```

---

## **Funciones**

### **`promptText(text)`**
- **Descripción**: Genera contenido de texto a partir de una cadena dada como input.
- **Parámetro**:
  - `text`: El texto que se utiliza como prompt para generar el contenido.
- **Retorno**: El texto generado por el modelo.

### **`promptFromImage(text, path)`**
- **Descripción**: Genera contenido a partir de una imagen y una descripción.
- **Parámetros**:
  - `text`: Texto descriptivo que se proporciona como contexto para la imagen.
  - `path`: Ruta al archivo de imagen que se carga para generar el contenido.
- **Retorno**: El contenido generado en función de la imagen y el texto.

### **`promptCode(text)`**
- **Descripción**: Genera código a partir de una descripción proporcionada.
- **Parámetro**:
  - `text`: Descripción del código que se desea generar.
- **Retorno**: El código generado por el modelo.

### **`conversation()`**
- **Descripción**: Inicia una conversación con el modelo en la que el usuario puede interactuar continuamente, proporcionando inputs. El historial de la conversación se guarda en un archivo `.md`.
- **Funcionamiento**:
  - El usuario puede interactuar con el modelo escribiendo en la consola.
  - Escribe `exit` para finalizar la conversación.
  - El historial se guarda en el archivo `conversation_history.md`.
  
### **`main_menu()`**
- **Descripción**: Menú interactivo que permite al usuario elegir una de las cinco opciones: generar texto, generar contenido desde una imagen, generar código, mantener una conversación, o salir del programa.
- **Opciones**:
  1. Generar texto.
  2. Generar contenido a partir de una imagen.
  3. Generar código.
  4. Mantener conversación con historial.
  5. Salir del programa.

---

## **Ejecución del Programa**

El programa comienza con la función `main_menu()`, que solicita al usuario seleccionar una opción de la lista disponible. Dependiendo de la opción seleccionada, se ejecuta una de las siguientes acciones:
- Generar texto a partir de un prompt.
- Generar contenido a partir de una imagen y una descripción.
- Generar código en función de una descripción.
- Iniciar una conversación con el modelo, donde las respuestas del usuario y del modelo se guardan en un archivo de historial.
- Salir del programa.

Para iniciar el programa, basta con ejecutar el archivo y seguir las instrucciones en la consola.

---

## **Uso del Archivo `conversation_history.md`**

Al seleccionar la opción de conversación, cada intercambio entre el usuario y el modelo se guarda en el archivo `conversation_history.md` en el siguiente formato:
- **`Tú:`** para el input del usuario.
- **`Modelo:`** para la respuesta generada por el modelo.

Al finalizar la conversación, este archivo se guarda automáticamente en el directorio del proyecto.

---

## **Requerimientos**
- **Paquete de Google Generative AI**: Para utilizar la API, es necesario tener configurada la clave de API (`api_key`).
- **Bibliotecas necesarias**:
  - `google.generativeai`
  - `os`

Asegúrate de tener las dependencias instaladas y configuradas antes de ejecutar el programa.
