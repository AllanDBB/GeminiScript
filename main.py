import google.generativeai as genai
import os

genai.configure(api_key="") # Pon tu API Key de OpenAI aquí.
imageTesting = "./images/racoel.png"
model = genai.GenerativeModel("gemini-1.5-flash")

def promptText(text):
    response = model.generate_content(text)
    return response.text

def promptFromImage(text, path):
    myfile = genai.upload_file(path)
    response = model.generate_content([myfile, "\n\n", text])
    return response.text
    
def promptCode(text):
    modelCode = genai.GenerativeModel(
    model_name='gemini-1.5-pro',
    tools='code_execution')

    response = modelCode.generate_content(text)
    return response.text

def conversation():
    history = []
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            break
        history.append(f"Tú: {user_input}")
        response = model.generate_content(user_input)
        history.append(f"Modelo: {response.text}")
        print(f"Modelo: {response.text}")
    
    # Guardar la conversación en un archivo .txt
    with open("conversation_history.md", "w") as file:
        for line in history:
            file.write(line + "\n")
    print("Conversación guardada en 'conversation_history.md'.")

# Menú principal
def main_menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Generar texto")
        print("2. Generar contenido desde una imagen")
        print("3. Generar código")
        print("4. Mantener conversación con historial")
        print("5. Salir")

        option = input("Ingrese el número de la opción: ")

        if option == "1":
            text = input("Ingrese el texto para generar: ")
            print(promptText(text))
        elif option == "2":
            text = input("Ingrese el texto para describir la imagen: ")
            print(promptFromImage(text, imageTesting))
        elif option == "3":
            text = input("Ingrese la descripción del código que desea generar: ")
            print(promptCode(text))
        elif option == "4":
            conversation()
        elif option == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()