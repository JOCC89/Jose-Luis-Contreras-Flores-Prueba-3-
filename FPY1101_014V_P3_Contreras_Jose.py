import os
os.system("cls")
import random

datos = []
print("***Automotora 'Auto Seguro'***\n")

def grabar():
    print("Guardar datos del vehículo\n")
    while True:
        tipo = input(
            "Ingrese el tipo de vehículo (Automóvil, Camión, Camioneta o Moto):\n").capitalize()
        if tipo not in ["Automovil", "Camion", "Camioneta", "Moto"]:
            print("No se ingresó dato correctamente, intente de nuevo")
            continue

        patente = input("Ingrese letras de la patente:\n").upper()
        patente2 = input("Ingrese los números de la patente:\n")
        if len(patente2) < 2 or len(patente2) > 3 or not patente2.isdigit():
            print("No se ingresó dato correctamente, intente de nuevo")
            continue

        marca = input("Ingrese marca del vehículo:\n")
        if len(marca) < 2 or len(marca) > 15:
            print("No se ingresó dato correctamente, por favor intente de nuevo")
            continue

        precio = int(input("Ingrese el precio del vehículo (debe ser mayor a 5,000,000):\n"))
        if precio < 5000000:
            print("Error, debe ingresar un numero mayor a 5 millones")
        

        try:
            multa = int(input("Ingrese el monto de la multa:\n"))
        except ValueError:
            print("Error: debe ingresar un número válido")
            continue

        multa_fecha = input("Ingrese la fecha de la multa (dd/mm/aaaa):\n")
        fecha_registro = input(
            "Ingrese fecha de registro del vehículo (dd/mm/aaaa):\n")

        try:
            run = int(
                input("Ingrese RUN sin guion ni dígito verificador (7-8 dígitos):\n"))
            if run < 1000000 or run > 99999999:
                raise ValueError
        except ValueError:
            print("RUN no válido, intente nuevamente")
            continue

        nombre = input("Ingrese nombre del dueño del vehículo:\n")
        apellido = input("Ingrese apellido del dueño del vehículo:\n")
        emision = input(
            "Ingrese el certificado de emisión de contaminantes:\n")
        anotaciones = input("Ingrese anotaciones vigentes:\n")

        
        patente_completa = patente + "-" + patente2
        datos[patente_completa] = {
            "tipo": tipo,
            "marca": marca,
            "precio": precio,
            "multa": multa,
            "multa_fecha": multa_fecha,
            "fecha_registro": fecha_registro,
            "run": run,
            "nombre": nombre,
            "apellido": apellido,
            "emision": emision,
            "anotaciones": anotaciones
        }

        
        print("Datos guardados con éxito")
        break


def buscar():
    print("Buscar auto por su patente")
    macht = input(
        "Ingrese el código de la patente que desea consultar (letras-números):\n").upper()
    if macht in datos:
        vehiculo = datos[macht]
        print(f"Tipo de vehículo: {vehiculo['tipo']}, Patente: {macht}, Marca: {vehiculo['marca']}, Precio: ${vehiculo['precio']}, Multas: ${vehiculo['multa']}, Fecha de registro: {vehiculo['fecha_registro']}, RUN: {vehiculo['run']}, Nombre: {vehiculo['nombre']}")
    else:
        print("Patente no definida")


def imprimir_certificado():
    print("Certificados vigentes")
    macht = input(
        "Ingrese el código de la patente que desea consultar (letras-números):\n").upper()
    if macht in datos:
        vehiculo = datos[macht]
        print(f"Emisión de contaminantes: {vehiculo['emision']}")
        print(f"Anotaciones vigentes: {vehiculo['anotaciones']}")
        for _ in range(3):
            print(f"Monto: ${random.randint(1500, 3500)}")
    else:
        print("Patente no definida")


def salir():
    print("Haz salido del sistema")
    print("Gracias por usar 'Auto Seguro'")


def mostrar_menu():
    print("1. Grabar datos")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")


def main():
    print("\nMenú tu Auto Seguro\n")
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nIngrese la opción que desee:\n"))
            if opcion < 1 or opcion > 4:
                raise ValueError
        except ValueError:
            print("Error, por favor ingrese un valor correcto")
            continue

        if opcion == 1:
            grabar()
        elif opcion == 2:
            buscar()
        elif opcion == 3:
            imprimir_certificado()
        elif opcion == 4:
            salir()
            break


# Ejecutar el menú principal
main()
