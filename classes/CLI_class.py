import cmd

#Clase que contendrá las funcionalidades de la CLI
class CLI(cmd.Cmd):
    prompt = 'CLI > '  # Aqui estoy definiendo el prompt de la CLI, esto sirve para que el usuario sepa que puede escribir un comando
    intro = 'Bienvenido a la CLI. Escribe help o ? para listar los comandos disponibles.'  # Mensaje inicial
    
    
# Para probar la CLI, creo una instancia de la clase CLI y llamo al método cmdloop(). 
# Este método sirve para iniciar el bucle de la CLI y esperar a que el usuario ingrese un comando.
if __name__ == '__main__':
    CLI().cmdloop()