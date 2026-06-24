import random
import string

# Lista para almacenar usuarios registrados
usuarios = []

def generar_contrasena():
  
    #Función que genera una contraseña automática según la longitud
   # ingresada por el usuario.
   
    print("Generador automático de contraseña")

    while True: # Bucle para asegurar que el usuario ingrese un número válido para la longitud de la contraseña
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))

            if longitud < 8: # La contraseña debe tener al menos 8 caracteres
                print("La contraseña debe tener al menos 8 caracteres.")
            else:# Si la longitud es válida, se sale del bucle
                break
        except ValueError: # Captura el error si el usuario ingresa un valor que no es un número entero
            print("Debe ingresar un número válido.")

    caracteres = string.ascii_letters + string.digits + string.punctuation # Conjunto de caracteres que se usarán para generar la contraseña

    contrasena_generada = "" # Variable para almacenar la contraseña generada

    for i in range(longitud):  # Bucle que se repite 'longitud' veces para generar cada carácter de la contraseña
        contrasena_generada += random.choice(caracteres) # Se elige un carácter aleatorio del conjunto de caracteres y se agrega a la contraseña generada

    return contrasena_generada # La función devuelve la contraseña generada al final de su ejecución


def registrar_usuario(): 

    #Función que permite registrar un usuario y elegir si desea
    #crear una contraseña automática o manual.
   
    print("Registro de usuario")

    usuario = input("Ingrese su nombre de usuario: ")

    opcion = input("¿Desea crear una contraseña automática? (s/n): ").lower()

    if opcion == "s": # Si el usuario elige crear una contraseña automática, se llama a la función generar_contrasena() para generar la contraseña y se muestra al usuario.
        contrasena = generar_contrasena() 
        print("Su contraseña generada es:", contrasena)

    elif opcion == "n":# Si el usuario elige crear una contraseña manual, se le solicita que ingrese su contraseña y se verifica si cumple con la longitud mínima de 8 caracteres.
        contrasena = input("Ingrese su contraseña: ")

        if len(contrasena) < 8: # Se verifica si la contraseña ingresada tiene menos de 8 caracteres y se muestra un mensaje de advertencia.
            print("Advertencia: la contraseña ingresada es débil porque tiene menos de 8 caracteres.")
        else:
            print("Contraseña registrada correctamente.")

    else: # Si el usuario ingresa una opción inválida, se muestra un mensaje de error y se cancela el registro.
        print("Opción inválida. Se canceló el registro.")
        return

    nuevo_usuario = { # Diccionario que almacena el nombre de usuario y la contraseña del usuario registrado.
        "usuario": usuario,
        "contrasena": contrasena
    }

    usuarios.append(nuevo_usuario) # Se agrega el nuevo usuario a la lista de usuarios registrados y se muestra un mensaje de confirmación.

    print("Usuario registrado correctamente.") 


def mostrar_usuarios():
   
    #Función que muestra los usuarios registrados.
    #Por seguridad no se muestra la contraseña completa.
  
    print("Usuarios registrados: ")

    if len(usuarios) == 0:# Se verifica si la lista de usuarios está vacía y se muestra un mensaje indicando que no hay usuarios registrados.
        print("No hay usuarios registrados.")
    else: # Si hay usuarios registrados, se recorre la lista de usuarios y se muestra el nombre de usuario y una representación oculta de la contraseña (con asteriscos) para cada usuario registrado.
        for usuario in usuarios:
            print("Usuario:", usuario["usuario"])
            print("Contraseña: ********")
            print("     ")


def menu():
    
    #Menú principal del programa.
    #Se repite hasta que el usuario decida salir.
    
    while True: # Bucle que se repite hasta que el usuario decida salir del programa.
        print("GENERADOR SEGURO DE CONTRASEÑAS")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")# Se solicita al usuario que seleccione una opción del menú y se almacena en la variable 'opcion'.

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Inicio del programa
menu()
