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


def mostrar_menu():
    print("\n--- Menú Principal del Registro de Empleados ---")
    print("1. Agregar Nuevo Empleado")
    print("2. Listar Todos los Empleados")
    print("3. Salir")
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
            print('\n---SALIENDO DEL SISTEMA--')
            break
        else:
            print('Seleccione una opcion valida')

main()