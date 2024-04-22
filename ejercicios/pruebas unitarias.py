"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */
"""
import unittest

def suma(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b 

class pruebas(unittest.TestCase):
    
    def testsum(self):
        self.assertEqual(sum(2,3),5)
        self.assertEqual(sum(-2,2),0)
        self.assertEqual(sum(2.2,2.2),4.4)
        self.assertEqual(sum(2,3),5)
        self.assertEqual(sum(2.3,3),5.3)
        
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)
            
