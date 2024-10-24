import unittest

from src.modulos import depresion

class TestPrevisionesDeDeprecioacion(unittest.TestCase):
    
    def test_valores_normales(self):
        resultados = depresion(10000, 2000, 5)
        self.assertEqual(resultados[0], (1, 2006, 1600.0, 1600.0, 8400.0))
        self.assertEqual(resultados[0], (2, 2007, 1600.0, 3200.0, 6800.0))
        self.assertEqual(resultados[0], (5, 20010, 1600.0, 8000.0, 2000.0))
    
    def test_valor_final_mayor(self):
        resultados = depresion(10000, 12000, 5)
        self.assertEqual(resultados[0], (1, 2006, -400.0, -400.0, 10400.0))
        self.assertEqual(resultados[4], (5, 2010, -400.0, -2000.0, 8800.0))
    
    def test_vida_util_cero(self):
        with self.assertRaises(ZeroDivisionError):
            depresion(10000, 2000, 0)

    def test_valores_negativos(self):
        resultados = depresion(-10000, -2000,5)
        self.assertEqual(resultados[0], (1, 2006, -1600.0, -1600.0, -8400.0))
        self.assertEqual(resultados[4], (5, 2010, -1600.0, -8000.0, -2000.0))

if __name__ == '__main__':
    unittest.main()