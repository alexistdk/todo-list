from Tarea import *
import os


class Menu:

    @staticmethod
    def menu_principal():
        opcion1 = "1. Agregar tarea"
        opcion2 = "2. Actualizar descripción"
        opcion3 = "3. Eliminar tarea"
        opcion4 = "4. Cambiar estado"
        opcion5 = "5. Listar tareas"
        opciones = [opcion1, opcion2, opcion3, opcion4, opcion5]
        for i in range(len(opciones)):
            print(opciones[i])

    @classmethod
    def elegir_opcion(cls):
        opcion = int(input("\nElija una opción: "))
        if opcion == 1:
            Tarea.agregar_tarea()
            cls.volver_al_menu()
        elif opcion == 2:
            Tarea.mostrar_tareas()
            Tarea.modificar_tarea()
            cls.volver_al_menu()
        elif opcion == 3:
            Tarea.mostrar_tareas()
            Tarea.eliminar_tarea()
            cls.volver_al_menu()
        elif opcion == 4:
            Tarea.mostrar_tareas()
            Tarea.cambiar_estado()
            cls.volver_al_menu()
        elif opcion == 5:
            Tarea.mostrar_tareas()
            cls.volver_al_menu()
        else:
            input("Opción incorrecta. Presione cualquier tecla para ingresar una opción válida")
            os.system('clear')
            cls.menu_principal()
            cls.elegir_opcion()

    @classmethod
    def volver_al_menu(cls):
        input("Presione cualquier tecla para continuar...")
        os.system('clear')
        cls.menu_principal()
        cls.elegir_opcion()

