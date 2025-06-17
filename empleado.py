class Empleado:
    def __init__(self, id_empleado, nombre, apellido, puesto, salario):

        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.salario = salario

    def obtener_informacion(self): #Este metodo tambien puede llamarse como toString
        return (f'ID: {self.id_empleado}, Nombre: {self.nombre} {self.apellido}, Puesto: {self.puesto}, Salario: ${self.salario:.2f}')
    

class SistemaRegistroEmpleados:

    def __init__(self):
        self.empleados = {}

    def agregar_empleados(self):
        print('\n--- Agregar Nuevo Empleado ---')
        while True:
            id_empleado = input('Ingrese el ID del empleado:\n')

            if not id_empleado:
                print('El ID de empleado no puede estar vacio. Intente de Nuevo')
                continue
            if id_empleado in self.empleados:
                print(f'Ya existe un empleado con el ID {id_empleado} por favor verifique nuevamente')
            else:
                break

        nombre = input('Ingrese el nombre del empleado:\n')
        apellido = input('Ingrese el apellido del empleado:\n')
        puesto = input('Ingrese el puesto del empleado:\n')

        while True:
            try:
                salario = float(input('Ingrese el salario del empleado: \n$ '))
                if salario < 0:
                    print('El salario no puede ser ni 0 ni un numero negativo')
                else:
                    break
            except ValueError:
                print('\nEntrada invalida. Por favor ingrese nuevamente el salario')

        nuevo_empleado = Empleado(id_empleado,nombre,apellido,puesto,salario)


        self.empleados[id_empleado] = nuevo_empleado
        print(f'\nEmpleado "{nombre} {apellido}" agregado con exito.') 

    def listar_empleados(self):
        print('\n--- Lista de Empleado ---')
        if not self.empleados:
            print('No hay empleados Registrados en el sistema')
            return
        for id_empleado, empleado in self.empleados.items():
            print(empleado.obtener_informacion())

    def borrar_empleado(self):
        print('\n --- Borrar Empleado ---')
        if not self.empleados:
            print('No hay empleado registrados')
            return
        id_a_borrar = input('Ingrese el ID del empleado a BORRAR:\n')
        if id_a_borrar in self.empleados:
            empleado_borrado = self.empleados.pop(id_a_borrar)
            print(f'Empleado {empleado_borrado.nombre} {empleado_borrado.apellido} ha sido ELIMINADO')

    def modificar_empleado(self):
        print('\n --- Modificar Empleado ---')
        if not self.empleados:
            print('No hay empleado registrados')
            return
        id_a_modificar = input('Ingrese el ID del empleado a MODIFICAR:\n')
        if id_a_modificar in self.empleados:
            empleado = self.empleados[id_a_modificar]
            print(f'Informacion del empleado actual: \n {empleado.obtener_informacion()}')
            print('\nIngrese los nuevos datos del empleado (deje en blanco para mantener la informacion)')
            nuevo_nombre = input(f'Nuevo Nombre: ({empleado.nombre})').strip()
            if nuevo_nombre:
                empleado.nombre = nuevo_nombre
            
            nuevo_apellido = input(f'Nuevo Apellido: ({empleado.apellido})').strip()
            if nuevo_apellido:
                empleado.apellido = nuevo_apellido
            
            nuevo_puesto = input(f'Nuevo Puesto: ({empleado.puesto})').strip()
            if nuevo_puesto:
                empleado.puesto = nuevo_puesto

            while True:
                nuevo_salario_str = input(f'Nuevo Salario ({empleado.salario:.2f}): ').strip()
                if not nuevo_salario_str:
                    break
                try:
                    nuevo_salario = float(nuevo_salario_str)
                    if nuevo_salario < 0:
                        print('El salario no puede ser ni 0 ni negativo. Intente de nuevo \n')
                    else:
                        empleado.salario = nuevo_salario
                        break
                except ValueError:
                    print('Entrada invalida, por favor ingrese un valor valido para salario')
            print(f'Empleado con la ID "{id_a_modificar}" ha sido modificado con exito')
            print(f'Nueva informacion: {empleado.obtener_informacion()}')

            


def mostrar_menu():
    print("\n--- Menú Principal del Registro de Empleados ---")
    print("1. Agregar Nuevo Empleado")
    print("2. Listar Todos los Empleados")
    print("3. Borrar empleado")
    print("4. Modificar empleado")    
    print("5. Salir")
    print("---------------------------------------------")

def main():
    sistema_registro = SistemaRegistroEmpleados()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == '1':
            sistema_registro.agregar_empleados()
        elif opcion == '2':
            sistema_registro.listar_empleados()
        elif opcion == '3':
            sistema_registro.borrar_empleado()
        elif opcion == '4':
            sistema_registro.modificar_empleado()        
        elif opcion == '5':
            print('\n---SALIENDO DEL SISTEMA--')
            break
        else:
            print('Seleccione una opcion valida')

main()