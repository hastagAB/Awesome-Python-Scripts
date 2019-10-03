from unittest import TestCase

from calc import soma, sub, mult, div


class testCalc(TestCase):
    def test_should_return_two_values_sum(self):
        esperado = 1 + 2
        self.assertEqual(esperado, soma(1,2))


    def test_should_return_two_values_sub(self):
        esperado = 1 - 2
        self.assertEqual(esperado, sub(1,2))


    def test_should_return_two_values_mult(self):
        esperado = 1 * 2
        self.assertEqual(esperado, mult(1,2))

    def test_should_return_two_values_div(self):
        esperado = 1 / 2
        self.assertEqual(esperado, div(1,2))


    def test_should_return_exceptio_on_division_by_zero(self):
        esperado = 'Divisao por zero mal sucedida!!'
        self.assertEqual(esperado, div(1,0))
