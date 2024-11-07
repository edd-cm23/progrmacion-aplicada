# tercer examen parcial
import os 

class Jugador:
    def __init__(self,nombre,añoNac,sexo,becado):
        self.nombre = nombre
        self.añoNac = añoNac
        self.sexo = sexo
        self.becado = becado

    def __str__(self):
        return f'Nombre: {self.nombre}, AñoNac: {self.añoNac}, Sexo: {self.sexo}, Becado: {self.becado}'


class Categoria:
    def __init__(self,nombre,rango,costo):
        self.Nombre = nombre
        self.Rango = rango 
        self.Costo = costo
        self.Jugadores = list()

    def agregar_jugador(self,jugador):
        self.Jugadores.append(jugador)

    def __str__(self):
        return  f'Nombre: {self.Nombre}, Rango: {self.Rango}, Costo: {self.Costo}'


class academia:
    def __init__(self,nombre,propietario,domicilio):
        self.Nombre = nombre
        self.Propietario = propietario
        self.Domicilio = domicilio       
        self.Categorias = list()
    
    def agregar_categoria(self,Categoria):
        self.Categorias.append(Categoria)

    def mh(self):
        nm = 0
        nh = 0
        for categoria in self.Categorias:
            for jugador in categoria.Jugadores:
                if jugador.sexo == 'Mujer':
                    nm += 1
                else:
                    nh += 1    

        return f'Hombres: {nh}\nMujeres: {nm}'    
    def pago_categoria(self):
            total = 0
            subtotal = []
            for categoria in self.Categorias:
                for jugador in categoria.Jugadores:
                    if jugador.becado != 'Becado':
                        total = total + categoria.Costo
                subtotal.append(total)
                total = 0        
            return subtotal
    
    def total_pagos(self):
        total = 0
        for categoria in self.Categorias:
            for jugador in categoria.Jugadores:
                if jugador.becado != 'Becado':
                    total = total + categoria.Costo
        return total       

    def __str__(self):
        return  f'Nombre: {self.Nombre}\nPropietario: {self.Propietario}\nDomicilio: {self.Domicilio}'     


la_academia = academia(nombre = 'Academia santos laguna', propietario = 'Francisco Nava', domicilio = 'aguanaval 123,hidraulica')

la_academia.agregar_categoria(Categoria(nombre= 'Junior A', rango=' 2006/2007/2008', costo= 1250.00))
la_academia.agregar_categoria(Categoria(nombre= 'Junior B', rango=' 2009/2010/2011', costo= 850.00))
la_academia.agregar_categoria(Categoria(nombre= 'Pony A', rango=' 2012/2013/2014', costo= 700.00))

la_academia.Categorias[0].agregar_jugador(Jugador(nombre= 'Alexander Lopez', añoNac = 2006, sexo = 'Hombre', becado = 'Sin Beca'))
la_academia.Categorias[0].agregar_jugador(Jugador(nombre= 'Uriel Puga', añoNac = 2007, sexo = 'Hombre', becado = 'Becado'))
la_academia.Categorias[0].agregar_jugador(Jugador(nombre= 'Alejandra Escalona', añoNac = 2008, sexo = 'Mujer', becado = 'Sin Beca'))
la_academia.Categorias[1].agregar_jugador(Jugador(nombre= 'Armando Santana', añoNac = 2009, sexo = 'Hombre', becado = 'Sin Beca'))
la_academia.Categorias[1].agregar_jugador(Jugador(nombre= 'Daniel Mijares', añoNac = 2010, sexo = 'Hombre', becado = 'Sin Beca'))
la_academia.Categorias[1].agregar_jugador(Jugador(nombre= 'Antonio Hernandez', añoNac = 2011, sexo = 'Hombre', becado = 'Becado'))
la_academia.Categorias[2].agregar_jugador(Jugador(nombre= 'Andrea Solis', añoNac = 2012, sexo = 'Mujer', becado = 'Becado'))
la_academia.Categorias[2].agregar_jugador(Jugador(nombre= 'Marissa Hernandez', añoNac = 2013, sexo = 'Mujer', becado = 'Becado'))
la_academia.Categorias[2].agregar_jugador(Jugador(nombre= 'Diana Soto', añoNac = 2014, sexo = 'Mujer', becado = 'Sin Beca'))

def main():
    os.system('cls')
    print(f'{la_academia}')
    print(f'\nTotal de Categorias: {len(la_academia.Categorias)}')
    print(f'{la_academia.mh()}')

    print('\nJugadores por Categoria:')
    for categoria in la_academia.Categorias:
        print(f'\n{categoria.Nombre} - {categoria.Rango} - {categoria.Costo}')
        for jugador in categoria.Jugadores:
            print(f'{jugador}')
        print(f'\nSubtotal por categoria: {la_academia.pago_categoria()[la_academia.Categorias.index(categoria)]}') 
        

    print(f'\ntotal pagos: ${la_academia.total_pagos()}')

if __name__ == '__main__':
    main()    