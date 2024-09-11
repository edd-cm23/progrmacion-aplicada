#Inscripciones a un evento académico

import os ; os.system("cls")

venta_dia = 0 

print('Universidad Patito SA de CV \nSistema de inscripcion Congreso de Sistemas\n')
  

while True:        
    print('tipo de usuario:\n[1] Alumno $100\n[2] Trabajador $200\n[3] Docente $500')
    
    usuario = int(input('Indica con un num el tipo de usuario: \n'))
    
    if usuario == 1:
        p_usuario = 100
        tipo_usuario = 'Alumno'
    elif usuario == 2:
        p_usuario = 200
        tipo_usuario = 'Trabajador'
    elif usuario == 3:
        p_usuario = 500
        tipo_usuario = 'Docente'
    else:
        print('No existe ese tipo usuario')
        continue
    
    print('\nSelecciona el tipo de paquete:\n[1] Solo conferencias $600\n[2] Con eventos sociales $800\n[3] Con kit de acceso $900')
    
   
    paquete = int(input('Escoge el paquete: '))
    
    if paquete == 1:
        p_paquete = 600
        tipo_paquete = "Solo conferencias"
    elif paquete == 2:
        p_paquete = 800
        tipo_paquete = "Con eventos sociales"
    elif paquete == 3:
        p_paquete = 900
        tipo_paquete = "Con kit de acceso"
    else:
        print('No contamos con ese paquete')
        continue
    
    cantidad = int(input("\nCantidad? "))
    
    subtotal = (p_usuario + p_paquete) * cantidad
     
    if subtotal > 5000:
        if usuario == 1:  
             total = subtotal * .8
    
        elif usuario == 2:  
             total = subtotal * .9
            
        elif usuario == 3:  
            total = subtotal * .95
    else:
        total = subtotal        
    
    print(f"\nTu pedido fue: {cantidad}\nTipo de usuario: {tipo_usuario}\nTipo de paquete: {tipo_paquete}")
    print(f"Subtotal: ${subtotal:,}\nDescuento de: ${subtotal - total:,} ({(1-(total / subtotal))*100:.1f}%)\nCon un total de: ${total:,}")
  
    venta_dia += total
    
    print('-'*35)

    continuar = input('\n¿Deseas continuar? ("S"/"N": \n')
    print('-'*35)
    if continuar.upper() == 'N':
        print(f'\nTotal de ventas: ${venta_dia:,}')
        print('Proceso terminado')
        break