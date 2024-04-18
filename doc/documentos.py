#DOCUMENTOS

class Documents():
    def __init__(self,nombre,fecha,tarea):
        self.nombre = nombre
        self.fecha = fecha
        self.tarea = tarea

    def agregar_tarea(self,nombre):
        print("""
            |=====================|
            |Vamos a agregar tarea|
            |=====================|
            """)
        
        opcion = input('¿Que cosas podria mejorar de la web?')
        
        
