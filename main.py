from BaseDeDatos import *
from Menu import *

if __name__ == '__main__':
    BaseDeDatos.conectar_a_ddbb()
    BaseDeDatos.crear_tabla_tareas()
    Menu.menu_principal()
    Menu.elegir_opcion()