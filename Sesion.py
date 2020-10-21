from BaseDeDatos import *
import os
from getpass import getpass
from Menu import *


class Sesion:

    @classmethod
    def iniciar_sesion(cls):
        os.system('clear')
        print("Iniciar sesión\n")
        nombre_usuario = input("Username: ")
        contrasenia = getpass(prompt="Constraseña: ")
        existe_usuario = BaseDeDatos.loguear_usuario(nombre_usuario, contrasenia)
        if existe_usuario:
            print("wawa")

    @classmethod
    def registrar_usuario(cls):
        os.system('clear')
        username = input("Nombre de usuario: ")
        email = input("Email: ")
        password = getpass(prompt="Contraseña: ")
        password_reingresada = getpass(prompt="Reingrese la contraseña: ")
        if password == password_reingresada:
            BaseDeDatos.registrar_usuario(username, email, password)
        else:
            input("Las contraseñas no coinciden. Intente nuevamente")
            cls.pantalla_principal()

    @classmethod
    def pantalla_principal(cls):
        os.system('clear')
        print("1. Iniciar sesión")
        print("2. Registrarse\n")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            cls.iniciar_sesion()
        elif opcion == 2:
            cls.registrar_usuario()
        else:
            input("Opción inválida. Intente nuevamente.")
            cls.pantalla_principal()
