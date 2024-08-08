import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiproducts as uisSt
def NewStudent():
    title = """
    *************************
    * REGISTRO DE PRODUCTOS *
    *************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input("Ingres el Nro de Id : ")
    codProdut = input("Ingrese Codigo del producto :")
    nombreproductost = input("Ingrese Nombre del producto : ")
    estudiante = {
        'identificacion': identificacion,
        'codProdut': codProdut,
        'nombreproductost': nombreproductost
    }
    cf.AddData('data',identificacion,estudiante)
    gf.PanCamp.get('data').update({identificacion:estudiante})
    if(bool(input('Desea registrar otro estudiante S(Si) o Enter(No)'))):
        NewStudent()
    else:
       uisSt.MenuStudent(0)

def SearchData():
    criterio = input('Ingrese el Nro Identificacion del estudiante: ')
    data=gf.PanCamp.get('data').get(criterio)
    return data
    

def ModifyData():
    dataprodut = SearchData()
    identificacion,codStudent,nombreStudent,notas = dataprodut.values()
    for key in dataprodut.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataprodut[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.PanCamp.get('data').update({identificacion:dataprodut})
    cf.UpdateFile(gf.PanCamp)
    uisSt.MenuProduct(0)