from unittest import TestCase

from calculo import calculo


class Test(TestCase):
    def test_calculo_passar(self):
        x = 1
        y = 2
        r = 1 * 2
        result = calculo(x, y)
        self.assertEquals(r, result)

    def test_deve_voltar_texto(self):
        x = 'a'
        y = 'b'
        result = calculo(x, y)
        esperado = 'not number'
        self.assertEqual(result, esperado)
