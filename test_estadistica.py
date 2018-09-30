from unittest import TestCase
from Estadistica import Estadistica

class TestEstadistica(TestCase):
    def test_dar_estadistica(self):
        self.assertEqual(Estadistica().dar_estadistica(""),[0,0,0,0],"Cadena vacia")

    def test_dar_estadistica_unacadena(self):
        self.assertEqual(Estadistica().dar_estadistica("1"),[1,0,0,0],"Un numero")

    def test_dar_estadistica_doscadenas(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2"), [2, 0, 0, 0], "dos numeros")

    def test_dar_estadistica_ncadenas(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2,3,4"), [4, 0, 0, 0], "n numeros")
