import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiproducts as uisSt
def NewProduct():
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
    producto = {
        'identificacion': identificacion,
        'codProdut': codProdut,
        'nombreproductost': nombreproductost
    }
    cf.AddData('data',identificacion,producto)
    gf.PanCamp.get('data').update({identificacion:producto})
    if(bool(input('Desea registrar otro producto S(Si) o Enter(No)'))):
        NewProduct()
    else:
       uisSt.MenuProduct(0)

def SearchData():
    criterio = input('Ingrese el Nro Identificacion del estudiante: ')
    data=gf.PanCamp.get('data').get(criterio)
    return data
    

def ModifyData():
    dataprodut = SearchData()
    identificacion,codprodut,nombreProduct,price = dataprodut.values()
    for key in dataprodut.keys():
        if (key != 'identificacion' and key != 'price'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataprodut[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.PanCamp.get('data').update({identificacion:dataprodut})
    cf.UpdateFile(gf.PanCamp)
    uisSt.MenuProduct(0)