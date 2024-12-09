import unittest
from numeroromano import converte

class TestNumeroRomano(unittest.TestCase):

    def test_conversoes(self):

        self.assertEqual(converte('I'), 1)
        self.assertEqual(converte('V'), 5)
        self.assertEqual(converte('II'), 2)
        self.assertEqual(converte('XXII'), 22)
        self.assertEqual(converte('IX'), 9)
        self.assertEqual(converte('XXIV'), 24)


    def test_invalido(self):
        
        self.assertEqual(converte('IIII'), 4)  # Aceitando até certo ponto (caso exótico)

if __name__ == "__main__":
    
    unittest.main()