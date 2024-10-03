import os ; os.system('cls')
# mes, día y nombre
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", 
                 "Octubre", "Noviembre", "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    mes = int(input('Introduce el número de mes: '))
    if 1 <= mes <= 12:
        nombre_mes =meses[mes - 1]  
        dias = dias[mes - 1]           

        print(f'mes: {nombre_mes}, {dias} días.')
        break
    else:
        print("Número de mes inválido. Debe estar entre 1 y 12.")
        pass

# import calendar 
# from calendar import monthrange

# mes = int(input())
# dias= monthrange(2023,mes)
# print(calendar.month_name[mes])
# print(dias[1])

