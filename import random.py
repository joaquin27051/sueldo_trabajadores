import random
import csv
import math

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández" ]
sueldos = {}

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)

def clasificar_sueldos():
    clasificaciones = {
        "menores_800k": [],
        "entre_800k_y_2M": [],
        "superiores_2M": []
    }
    
    total_sueldos = 0
    
    for trabajador, sueldo in sueldos.items():
        total_sueldos += sueldo
        if sueldo < 800000:
            clasificaciones["menores_800k"].append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            clasificaciones["entre_800k_y_2M"].append((trabajador, sueldo))
        else:
            clasificaciones["superiores_2M"].append((trabajador, sueldo))
    for categoria, empleados in clasificaciones.items():
        print(f"Sueldos {categoria.replace('_', ' ')} TOTAL: {len(empleados)}")
        for empleado, sueldo in empleados:
            print(f"{empleado} ${sueldo:,}")
    
    print(f"TOTAL SUELDOS: ${total_sueldos:,}")

def ver_estadisticas():
    if not sueldos:
        print("No hay sueldos asignados.")
        return
    
    sueldos_lista = list(sueldos.values())
    sueldo_max = max(sueldos_lista)
    sueldo_min = min(sueldos_lista)
    promedio = sum(sueldos_lista) / len(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos_lista) / len(sueldos_lista))

    print(f"Sueldo más alto: ${sueldo_max:,}")
    print(f"Sueldo más bajo: ${sueldo_min:,}")
    print(f"Promedio de sueldos: ${promedio:,.2f}")
    print(f"Media geométrica: ${media_geometrica:,.2f}")

def reporte_sueldos():
    with open("reporte_sueldos.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Trabajador", "Sueldo Bruto", "Sueldo Líquido"])
        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            
            writer.writerow([trabajador, sueldo, sueldo_liquido])
    
    print("Reporte de sueldos exportado a 'reporte_sueldos.csv'")

def salir_programa():
    print("Hasta pronto")
    print("Desarrollado por Joaquin Pastenes")
    print("RUT 220597393")

def main():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente")
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            salir_programa()
            break
        else:
            print("Opción no válida. Intente nuevamente")
main()
