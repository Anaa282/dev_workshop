class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_l = []
        for c in texto:
            if c.isalnum():
                texto_l.append(c.lower())

        return texto_l == texto_l[::-1]
        pass
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertido = ""
        for c in texto:
            invertido = c + invertido
        return invertido    
        pass
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        cont = 0
        for c in texto:
            if c in vocales:
                cont += 1
        return cont        
        pass
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        voc = "aeiou"
        cont = 0
        for c in texto.lower():
            if c.isalpha() and c not in voc:
                cont += 1
        return cont        

        pass
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        filtro1 = sorted(c.lower() for c in texto1 if c.isalnum())
        filtro2 = sorted(c.lower() for c in texto2 if c.isalnum())

        return filtro1 == filtro2

        pass
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        return len(texto.split())
        pass
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        return texto.title()
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """

        resultado = []
        espacio = False

        for char in texto:
            if char == " ":
                if not espacio:
                    resultado.append(char)
                espacio = True
            else:
                resultado.append(char)
                espacio = False
        return "".join(resultado)        
    

    pass
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
   
        if texto[0] in "+-":
            texto = texto[1:]

        for letra in texto:
            if letra < "0" or letra > "9":
                return False
        return True    

        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        if not texto:
            return None
        
        cifrado = ""

        for char in texto:
            if char.isalpha():
                if char.islower():
                    cifrado += chr((ord(char) - ord("a") + 2) % 26 + ord("a"))
                else:
                    cifrado += chr((ord(char) - ord("A") + 2) % 26 + ord("A"))

        return cifrado            
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        if not texto:
            return None
        
        descifrado = []

        for char in texto:
            if char.isalpha():
                if char.islower():
                    new = chr(((ord(char) - ord('a') - desplazamiento) % 26) + ord('a'))
                else:
                    new = chr(((ord(char) - ord('A') - desplazamiento) % 26) + ord('A'))
            else:
                new = char

            descifrado.append(new) 

        return "".join(descifrado)
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        posicion = []
        l_texto = len(texto)
        l_sub = len(subcadena)

        for i in range(l_texto - l_sub + 1):
            if texto[i:i + l_sub] == subcadena:
                posicion.append(i)
        return posicion        

        pass