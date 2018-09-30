from unittest import TestCase
from Estadistica import Estadistica

class TestEstadistica(TestCase):
    def test_dar_estadistica(self):
        self.assertEqual(Estadistica().dar_estadistica(""),[0,0,0,0],"Cadena vacia")

    def test_dar_estadistica_unacadena(self):
        self.assertEqual(Estadistica().dar_estadistica("1"),[1,1,1,0],"Un numero")

    def test_dar_estadistica_doscadenas(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2"), [2, 1, 2, 0], "dos numeros")

    def test_dar_estadistica_ncadenas(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2,3,4"), [4, 1, 4, 0], "n numeros")

    def test_dar_estadistica_minimo_vacio(self):
        self.assertEqual(Estadistica().dar_estadistica(""), [0, 0, 0, 0], "cadena vacia")

    def test_dar_estadistica_minimo_unnumero(self):
        self.assertEqual(Estadistica().dar_estadistica("4"), [1, 4, 4, 0], "Un numero")

    def test_dar_estadistica_minimo_dosnumeroa(self):
        self.assertEqual(Estadistica().dar_estadistica("4,8"), [2, 4, 8, 0], "minimo dos numeros")

    def test_dar_estadistica_minimo_nnumeros(self):
        self.assertEqual(Estadistica().dar_estadistica("1,8,7,6"), [4, 1, 8, 0], "minimo N numeros")

    def test_dar_estadistica_maximo_vacio(self):
        self.assertEqual(Estadistica().dar_estadistica(""), [0, 0, 0, 0], "cadena vacia")

    def test_dar_estadistica_maximo_unnumero(self):
        self.assertEqual(Estadistica().dar_estadistica("3"), [1, 3, 3, 0], "maximo un numero")

    def test_dar_estadistica_maximo_dosnumeroa(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2"), [2, 1, 2, 0], "maximo dos numeros")

    def test_dar_estadistica_maximo_nnumeros(self):
        self.assertEqual(Estadistica().dar_estadistica("1,2,3,4"), [4, 1, 4, 0], "maximo N numeros")

    def test_dar_estadistica_promedio_vacio(self):
        self.assertEqual(Estadistica().dar_estadistica(""), [0, 0, 0, 0], "cadena vacia")

