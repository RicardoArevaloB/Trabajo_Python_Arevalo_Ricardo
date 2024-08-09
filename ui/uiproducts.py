import modules.corefiles as cf
import funciones.globales as gf
import funciones.products as st
import main

def MenuProduct(op : int):
    title = """
    *******************************
    * GESTION DE VENTAS Y COMPRAS *
    *******************************
    """
    menuProductOp = '1. Agregar\n2. Editar\n3. Salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuProductOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            MenuProduct(0)
        else:
            match (op):
                case 1:
                    st.NewProduct()
                case 2:
                    st.ModifyData()
                case 3:
                    main.mainMenu(0)
                case _:
                    print("La opcion ingresada no esta disponible en las opciones")
                    gf.pausar_pantalla()