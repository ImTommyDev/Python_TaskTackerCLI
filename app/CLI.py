import cmd
import os
import time
from task import Task
from prettytable import PrettyTable

#Clase que contendrá las funcionalidades de la CLI
class CLI(cmd.Cmd):
    prompt = 'CLI > '  # Aqui estoy definiendo el prompt de la CLI, esto sirve para que el usuario sepa que puede escribir un comando
    intro = 'Bienvenido a la CLI. Escribe help o ? para listar los comandos disponibles'  # Mensaje inicial
      
          #Creación de un comando para mostrar al usuario el comando | para que sirve | ejemplo de como usarlo
    def do_comandos(self, line):
        """Muestra información sobre todos los comandos."""
        #TODO: Actualizar la documentación de todos los comandos
        comandos = {
            'help / ?': {
                'descripcion': 'Muestra todos los comandos.',
                'ejemplo-uso': 'help',
                'argumentos': 'Ninguno'
            },
            'comandos': {
                'descripcion': 'Muestra información sobre todos los comandos.',
                'ejemplo-uso': 'comandos',
                'argumentos': 'Ninguno'
            },
            'exit': {
                'descripcion': 'Sale de la CLI.',
                'ejemplo-uso': 'exit',
                'argumentos': 'Ninguno'
            },
            'add <tarea>':{
                'descripcion': 'Añade una tarea.',
                'ejemplo-uso': 'add Descripcion de la tarea',
                'argumentos': 'Descripcion de la tarea'
            },
            'list <estado>':{
                'descripcion': 'Si no se especifica un estado, lista todas las tareas.',
                'ejemplo-uso': 'list | list pendiente',
                'argumentos': 'OPCIONAL: pendiente, en progreso, completada'
            },
            'delete <id>':{
                'descripcion': 'Eliminar una tarea a través de su ID',
                'ejemplo-uso': 'delete 1',
                'argumentos': 'ID de la tarea'
            }
        }
        
        #Voy a mostrar los comandos con una table
        tabla = PrettyTable()
        tabla.field_names = ["Comando", "Descripción", "Ejemplo de uso", "Argumentos"]
        for comando, info in comandos.items():
            tabla.add_row([comando, info['descripcion'], info['ejemplo-uso'], info['argumentos']])
            
        print(tabla)
            
    #Comando para añadir tareas, 
    def do_add(self, descripcion):
        """"Añade una tarea."""
        task = Task()
        
        creada, id = task.add_task(descripcion)
        
        if creada:
            print(f"Tarea añadida: {descripcion} (ID: {id})")
        else:
            print("Error al añadir la tarea.")
    
    def do_list(self, estado):
        """Lista las tareas. Si no se especifica un estado, lista todas las tareas."""
        
        #Compruebo si se le ha pasado el estado o no, el resto de comprobaciones las haré en el métodod de la clase
        if estado:
            #Si se le pasa un estado, muestro solo las tareas con ese estado
            Task.list_tasks(estado)
            
        else:
            #Si no se especifica un estado, muestro todas las tareas
            Task.list_tasks()
            
    def do_delete(self,id):
        """Eliminar una tarea a través de su ID"""
        if Task.delete_task(id):
            print(f"Tarea con ID {id} eliminada.")
        
        
    
    def do_exit(self, line):
        """Sale de la CLI."""
        print('Saliendo de la CLI...')
        
        time.sleep(0.5)
        return True
            
    
    
# Para probar la CLI, creo una instancia de la clase CLI y llamo al método cmdloop(). 
# Este método sirve para iniciar el bucle de la CLI y esperar a que el usuario ingrese un comando.
if __name__ == '__main__':
    CLI().cmdloop()