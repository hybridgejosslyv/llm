from app.features.writing_assistant import generate_email, improve_text

def run():
    print("1. Generar correo")
    print("2. Mejorar texto")

    option = input("Selecciona una opción: ")

    if option == "1":
        topic = input("Tema del correo: ")
        result = generate_email(topic)
        print("\nResultado:\n", result)

    elif option == "2":
        text = input("Texto a mejorar: ")
        result = improve_text(text)
        print("\nResultado:\n", result)

    else:
        print("Opción no válida")