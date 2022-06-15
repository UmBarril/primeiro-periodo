import unittest
from Reforma import CalculaCusto, CalculaDesconto

class Tester(unittest.TestCase):
    def testar_CalculaCusto(self):
        porcelanato_valor = 69.90
        madeira_valor = 50.0
        ceramica_valor = 43.20
        # sem desconto
        self.assertAlmostEqual(CalculaCusto(1, "porcelanato"), porcelanato_valor)
        self.assertAlmostEqual(CalculaCusto(1, "madeira"), madeira_valor)
        self.assertAlmostEqual(CalculaCusto(1, "cerâmica"), ceramica_valor)
        
        # com desconto
        quant = 60
        valor_esperado_sem_desc = porcelanato_valor * quant
        valor_esperado = valor_esperado_sem_desc - (valor_esperado_sem_desc * 0.05)
        self.assertAlmostEqual(CalculaCusto(quant, "porcelanato"), valor_esperado)

    def testar_CalculaDesconto(self):
        self.assertEqual(CalculaDesconto(21, "porcelanato"), 0.05)
        self.assertEqual(CalculaDesconto(36, "madeira"), 0.08)
        self.assertEqual(CalculaDesconto(51, "cerâmica"), 0.10)

if __name__ == '__main__':
    unittest.main()