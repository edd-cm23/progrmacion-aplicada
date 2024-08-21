# Calcular la paga total de un trabajador
print('Calculando la paga de un trabajador\n')
nombre = input('Nombre : ')
horas = int(input('Horas trabajadas : '))
paga = float(input('Paga por hora : '))
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto
print('Resumen de pagos:\n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%')
print(f'Paga bruta {pagabruta :,.2f}') # con ":" incias a darle formato "," da formato a los miles y ".2f" pone dos decimales despues del punto
print(f'Impuessto {impuesto}')
print(f'Paga neta {paganeta}')