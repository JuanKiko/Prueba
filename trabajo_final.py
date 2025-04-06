class Libro:  
    def __init__(self, titulo, autor, isbn):  
        self.titulo = titulo  
        self.autor = autor  
        self.isbn = isbn  
        self.disponible = True  

    def agregar(self):  
        print(f"Libro '{self.titulo}' agregado con éxito.")  
        
    def prestar(self):  
        if self.disponible:  
            self.disponible = False  
            print(f"Libro '{self.titulo}' prestado con éxito.")  
        else:  
            print(f"El libro '{self.titulo}' ya está prestado.")  

    def devolver(self):  
        if not self.disponible:  
            self.disponible = True  
            print(f"Libro '{self.titulo}' devuelto con éxito.")  
        else:  
            print(f"El libro '{self.titulo}' ya estaba disponible.")  

    def mostrar(self):  
        estado = "Sí" if self.disponible else "No"  
        return f"- {self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"  

    def buscar(self):  
        return self.mostrar()  

def main():  
    biblioteca = []  
    
    print("Bienvenido al Sistema de Gestión de Biblioteca")  
    
    while True:  
        print("\nMenú:")  
        print("1. Agregar libro")  
        print("2. Prestar libro")  
        print("3. Devolver libro")  
        print("4. Mostrar libros")  
        print("5. Buscar libro por ISBN")  
        print("6. Salir")  
        
        opcion = input("Elige una opción: ")  
        
        if opcion == '1':  
            titulo = input("Título: ")  
            autor = input("Autor: ")  
            isbn = input("ISBN: ")  
            libro = Libro(titulo, autor, isbn)  
            libro.agregar()  
            biblioteca.append(libro)  
            
        elif opcion == '2':  
            isbn = input("Ingresa el ISBN: ")  
            libro_encontrado = next((libro for libro in biblioteca if libro.isbn == isbn), None)  
            if libro_encontrado:  
                libro_encontrado.prestar()  
            else:  
                print("ISBN no encontrado.")  
                
        elif opcion == '3':  
            isbn = input("Ingresa el ISBN: ")  
            libro_encontrado = next((libro for libro in biblioteca if libro.isbn == isbn), None)  
            if libro_encontrado:  
                libro_encontrado.devolver()  
            else:  
                print("ISBN no encontrado.")  
                
        elif opcion == '4':  
            for libro in biblioteca:  
                print(libro.mostrar())  
                
        elif opcion == '5':  
            isbn = input("Ingresa el ISBN: ")  
            libro_encontrado = next((libro for libro in biblioteca if libro.isbn == isbn), None)  
            if libro_encontrado:  
                print(libro_encontrado.buscar())  
            else:  
                print("ISBN no encontrado.")  
                
        elif opcion == '6':  
            print("Saliendo del programa.")  
            break  
            
        else:  
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")  

if __name__ == "__main__":  
    main()  
