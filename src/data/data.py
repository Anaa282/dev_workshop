class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_inv = []
        for elemento in lista:
            lista_inv.insert(0,elemento)
        return lista_inv    

        
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lista_sin_dup = []
        for elemento in lista:
            if not any(e is elemento for e in lista_sin_dup):
                lista_sin_dup.append(elemento)
        return lista_sin_dup        

        
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        i, j = 0, 0
        lista_ordenada = []

        while i<len(lista1) and j<len(lista2):
            if lista1[i] < lista2[j]:
                lista_ordenada.append(lista1[i])
                i+=1
            else:
                lista_ordenada.append(lista2[j])
                j+=1

        lista_ordenada.extend(lista1[i:])
        lista_ordenada.extend(lista2[j:])

        return lista_ordenada       


        pass
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return lista
        
        k = k % len(lista)
        
        return lista[-k:] + lista[:-k]
        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
       
        n = len(lista) + 1

        suma1 = n*(n+1)/2
        suma2 = sum(lista)

        return suma1-suma2
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True


        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []

        def is_empty():
            return len(pila)==0

        def push(elemento):
            pila.append(elemento)

        def pop():
            if not is_empty():
                return pila.pop()
            return None
        
        def peek():
            if not is_empty():
                return pila[-1]
            return None
        
        return{
            "push":push, "pop": pop, "peek": peek, "is_empty": is_empty

        }
        
        


        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola = []

        def is_empty():
            return len(cola) == 0
        
        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            if is_empty():
                return None
            return cola.pop(0)
        
        def peek():
            if is_empty():
                return None
            return cola[0]
        
        return{
            "enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty
        }


        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:
            return []
        
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = [[0]*filas for _ in range(columnas)]

        for i in range(filas):
            for j in range(columnas):
                transpuesta[j][i] = matriz[i][j]
        return transpuesta        


        pass