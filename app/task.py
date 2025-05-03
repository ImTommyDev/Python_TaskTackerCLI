import os
import json
from datetime import datetime
from prettytable import PrettyTable

ESTADOS = ["pendiente", "en progreso", "completada"]  # Lista de estados posibles para las tareas
ARCHIVO = 'tasks.json'  # Nombre del archivo JSON donde se guardarán las tareas

#Creo una clase Task que contendrá los atributos y métodos necesarios para crear una tarea.
class Task():    
    
    def generar_id(self):
        if not os.path.exists(ARCHIVO):
            return 1  # Si no existe el archivo, el primer id es 1

        try:
            with open(ARCHIVO, 'r') as archivo:
                datos = json.load(archivo)
                if datos:
                    ids = [tarea['id'] for tarea in datos]
                    max_id = max(ids) if ids else 0
                    return max_id + 1
                else:
                    return 1
        except json.JSONDecodeError:
            # Archivo vacío o mal formado
            return 1
        
    #Función que permite añadir una tarea, esta función debe crear el archivo .json y añadir la tarea al archivo .json en el caso de este no exista
    def add_task(self, descripcion):
        self.descripcion = descripcion
        self.estado = ESTADOS[0] # Estado inicial de la tarea es "pendiente"
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.fecha_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        #Compruebo si el archivo .json existe, si no existe lo crearé y añadiré la tarea
        if os.path.exists(ARCHIVO):
            try:
                #Si el archivo sí existe, lo abro, obtengo el id de la tarea y añado esta al archivo .json
                with open(ARCHIVO, 'r+') as archivo:
                    #Compruebo si el archivo .json tiene contenido
                    try:
                        tareas = json.load(archivo)
                    except json.JSONDecodeError:
                        tareas = []  # Si el archivo está vacío o malformado, empieza una lista nueva               
                                        
                    self.id = self.generar_id()
                    
                    #Creo un diccionario con los datos de la tarea
                    tarea = {
                        "id": self.id,
                        "descripcion": self.descripcion,
                        "estado": self.estado,
                        "fecha_creacion": self.fecha_creacion,
                        "fecha_update": self.fecha_update
                    }
                    
                    #Añado la tarea nueva a la lista de tareas (a la lista de diccionarios)
                    tareas.append(tarea)
                    
                    #Añado la tarea al archivo .json
                    archivo.seek(0) # Muevo el cursor al inicio del archivo para sobrescribirlo
                    json.dump(tareas, archivo, indent=4)
                    archivo.truncate() # Elimina el contenido del archivo después de escribir el nuevo contenido

                    return True, self.id 
                    
            except Exception as ex:
                print(f"Error al añadir la tarea: {ex}")
                return False
        else:
            #Si el archivo no existe, lo creo y añado la tarea
            with open(ARCHIVO, 'w') as archivo:
                #Obtengo el id de la tarea
                self.id = self.generar_id()
                
                #Creo un diccionario con los datos de la tarea
                tarea = {
                    "id": self.id,
                    "descripcion": self.descripcion,
                    "estado": self.estado,
                    "fecha_creacion": self.fecha_creacion,
                    "fecha_update": self.fecha_update
                }
                
                #Añado la tarea al archivo .json
                json.dump([tarea], archivo, indent=4) #dump convierte el diccionario en un objeto JSON y lo guarda en el archivo .json
                
                return True, self.id
            
    #Función para listar tareas
    def list_tasks(estado=None):
        
        #Si el estado que se le pasa es correcto, se listan las tareas con ese estado
        #Paso el estado a minúsculas para evitar problemas de mayúsculas y minúsculas
        estado = estado.lower() if estado else None
        if estado and estado in ESTADOS:
            with open(ARCHIVO , 'r') as archivo:
                tareas = json.load(archivo)
                
                tabla = PrettyTable()
                tabla.field_names = ["ID", "Descripcion", "Estado", "Fecha de Creación", "Fecha de Actualización"]
                
                for tarea in tareas:
                    if tarea['estado'] == estado:
                        tabla.add_row([f"{tarea['id']}", f"{tarea['descripcion']}", f"{tarea['estado']}", f"{tarea['fecha_creacion']}", f"{tarea['fecha_update']}"])
                        
                if tabla.rowcount == 0:
                    print(f"\n{' No hay tareas con el estado ' + estado + ' ':=^100}\n")
                else:
                    print(tabla)
        #Si se le pasa un estado pero no es correcto, muestro un error
        elif estado and estado not in ESTADOS:
            print(f"El estado {estado} no existe. Los estados posibles son: {', '.join(ESTADOS)}")
        #Si no se le pasa estado, se listan todas las tareas
        else:
            with open(ARCHIVO , 'r') as archivo:
                tareas = json.load(archivo)
                #creo una tabla para mostrar las tareas
                tabla = PrettyTable()
                tabla.field_names = ["ID", "Descripcion", "Estado", "Fecha de Creación", "Fecha de Actualización"]
                for tarea in tareas:
                    tabla.add_row([f"{tarea['id']}", f"{tarea['descripcion']}", f"{tarea['estado']}", f"{tarea['fecha_creacion']}", f"{tarea['fecha_update']}"])
                    
                print(tabla)
            
    