import cmd
import os
import time
from task import Task

#Clase que contendrá las funcionalidades de la CLI
class CLI(cmd.Cmd):
    prompt = 'CLI > '  # Aqui estoy definiendo el prompt de la CLI, esto sirve para que el usuario sepa que puede escribir un comando
    intro = 'Bienvenido a la CLI. Escribe help o ? para listar los comandos disponibles'  # Mensaje inicial
      
    #Comando para añadir tareas, 
    def do_add(self, descripcion):
        """"Añade una tarea."""
        task = Task()
        
        if task.add_task(descripcion):
            print(f"Tarea añadida: {descripcion}")
        else:
            print("Error al añadir la tarea.")
    
    def do_exit(self):
        """Sale de la CLI."""
        print('Saliendo de la CLI...')
        
        time.sleep(0.5)
        return True
        
    #Creación de un comando para mostrar al usuario el comando | para que sirve | ejemplo de como usarlo
    def do_comandos(self, line):
        """Muestra información sobre todos los comandos."""
        #TODO: Actualizar la documentación de todos los comandos
        comandos = {
            'help / ?': {
                'descripcion': 'Muestra todos los comandos.',
                'ejemplo-uso': 'help'
            },
            'comandos': {
                'descripcion': 'Muestra información sobre todos los comandos.',
                'ejemplo-uso': 'comandos'
            },
            'exit': {
                'descripcion': 'Sale de la CLI.',
                'ejemplo-uso': 'exit'
            },
            'add':{
                'descripcion': 'Añade una tarea.',
                'ejemplo-uso': 'add "Descripcion de la tarea"'
            }
        }
        
        for comando, info in comandos.items():
            print("-"*50)
            print(f"""Comando: {comando}
Descripcion: {info['descripcion']}
Ejemplo de uso: {info['ejemplo-uso']}\n""")
            
    
    
# Para probar la CLI, creo una instancia de la clase CLI y llamo al método cmdloop(). 
# Este método sirve para iniciar el bucle de la CLI y esperar a que el usuario ingrese un comando.
if __name__ == '__main__':
    CLI().cmdloop()