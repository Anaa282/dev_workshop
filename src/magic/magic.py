import math
class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n<=0:
            return 0
        elif n ==1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
        pass
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        secuencia = [0, 1]
        for _ in range(n - 2):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]


        pass
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        pass
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos = []
        for num in range(2, n + 1):
            es_primo = True
            for i in range(2, num):
                if num % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.append(num)
        return primos
        pass
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False
        
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n

        pass
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas < 1:
            return []
        
        triangulo = [[1]]
        for i in range(1,filas):
            fila_ant = triangulo[-1]
            nueva_f = [1]

            for j in range(1, len(fila_ant)):
                nueva_f.append(fila_ant[j-1] + fila_ant[j])


            nueva_f.append(1)
            triangulo.append(nueva_f)

        return triangulo    
             
        pass
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n == 0 or n == 1:
            return 1
        return n*self.factorial(n-1)

        pass
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        
        return math.gcd(a, b)
        pass
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
    
        return abs(a*b)//math.gcd(a, b)
        pass
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(d) for d in str(abs(n)))
        pass
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        digitos = len(str(n))
        suma = sum(int(d)**digitos for d in str(n))
        return suma == n
        pass
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)

        if any(len(fila) != n for fila in matriz):
            return False
        
        suma = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma:
                return False
            
        for cola in range(n):
            if sum(matriz[fila][cola] for fila in range(n)) != suma:
                return False
            
        if sum(matriz[i][i] for i in range(n)) != suma:
            return False
        
        if sum(matriz[i][n-i-1] for i in range(n)) != suma:
            return False
        
        return True

        pass