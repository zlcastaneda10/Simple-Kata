from unittest import TestCase
from Estadistica import Estadistica

class TestEstadistica(TestCase):
    def test_dar_estadistica(self):
        self.assertEqual(Estadistica().dar_estadistica(""),[0,0,0,0],"Cadena vacia")
