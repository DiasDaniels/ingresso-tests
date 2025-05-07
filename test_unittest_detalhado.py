import unittest
from uni_tst import calcular_valor_tickets

class TestCalcularValorTickets(unittest.TestCase):

    def test_TC01_infantis(self):
        self.assertEqual(calcular_valor_tickets(3, [5, 10, 12]), "Valor total: R$ 30")

    def test_TC02_adultos(self):
        self.assertEqual(calcular_valor_tickets(2, [30, 59]), "Valor total: R$ 60")

    def test_TC03_idosos(self):
        self.assertEqual(calcular_valor_tickets(2, [60, 80]), "Valor total: R$ 30")

    def test_TC04_misto(self):
        self.assertEqual(calcular_valor_tickets(3, [10, 30, 70]), "Valor total: R$ 55")

    def test_TC05_qtd_zero(self):
        self.assertEqual(calcular_valor_tickets(0, []), "Nenhum ticket adicionado!")

    def test_TC06_qtd_maior_que_5(self):
        self.assertEqual(calcular_valor_tickets(6, [10, 20, 30, 40, 50, 60]), "Quantidade máxima excedida!")

    def test_TC07_qtd_negativa(self):
        self.assertEqual(calcular_valor_tickets(-1, []), "Quantidade máxima excedida!")

    def test_TC08_idade_negativa(self):
        with self.assertRaises(ValueError):
            calcular_valor_tickets(1, [-5])

    def test_TC09_idade_maior_que_100(self):
        with self.assertRaises(ValueError):
            calcular_valor_tickets(1, [105])

    def test_TC10_limite_12_13(self):
        self.assertEqual(calcular_valor_tickets(2, [12, 13]), "Valor total: R$ 40")

    def test_TC11_idade_100(self):
        self.assertEqual(calcular_valor_tickets(1, [100]), "Valor total: R$ 15")

    def test_TC12_idade_0(self):
        self.assertEqual(calcular_valor_tickets(1, [0]), "Valor total: R$ 10")

    def test_BV01_qtd_zero(self):
        self.assertEqual(calcular_valor_tickets(0, []), "Nenhum ticket adicionado!")

    def test_BV02_qtd_um(self):
        self.assertEqual(calcular_valor_tickets(1, [30]), "Valor total: R$ 30")

    def test_BV03_qtd_cinco(self):
        self.assertEqual(calcular_valor_tickets(5, [10, 20, 30, 40, 50]), "Valor total: R$ 130")

    def test_BV04_qtd_seis(self):
        self.assertEqual(calcular_valor_tickets(6, [10, 10, 10, 10, 10, 10]), "Quantidade máxima excedida!")

    def test_BV05_idade_menos_um(self):
        with self.assertRaises(ValueError):
            calcular_valor_tickets(1, [-1])

    def test_BV06_idade_zero(self):
        self.assertEqual(calcular_valor_tickets(1, [0]), "Valor total: R$ 10")

    def test_BV07_idade_12(self):
        self.assertEqual(calcular_valor_tickets(1, [12]), "Valor total: R$ 10")

    def test_BV08_idade_13(self):
        self.assertEqual(calcular_valor_tickets(1, [13]), "Valor total: R$ 30")

    def test_BV09_idade_59(self):
        self.assertEqual(calcular_valor_tickets(1, [59]), "Valor total: R$ 30")

    def test_BV10_idade_60(self):
        self.assertEqual(calcular_valor_tickets(1, [60]), "Valor total: R$ 15")

    def test_BV11_idade_100(self):
        self.assertEqual(calcular_valor_tickets(1, [100]), "Valor total: R$ 15")

    def test_BV12_idade_101(self):
        with self.assertRaises(ValueError):
            calcular_valor_tickets(1, [101])

class CustomTextTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.successes = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalcularValorTickets)
    runner = unittest.TextTestRunner(verbosity=2, resultclass=CustomTextTestResult)
    result = runner.run(suite)

    print("\nResumo do Resultado:")
    print(f"✔️  Testes Passaram: {len(result.successes)}")
    print(f"❌  Testes Falharam: {len(result.failures)}")
    print(f"💥  Erros de Execução: {len(result.errors)}")