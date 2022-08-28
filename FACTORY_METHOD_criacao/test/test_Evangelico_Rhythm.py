try:
    import sys, os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise

import unittest
from Project.Ritimo_resource.Evangelico_Rhythm import EvangelicoRythm


class TestEvangelicoRythm(unittest.TestCase):
    def setUp(self) -> None:
        self.resultado_esperado = 'Tocando Musica Evangelica'
        self.radio = EvangelicoRythm()

    def test_if_function_tocar_musica_is_playing_evangelico(self):
        self.assertEqual(self.radio.tocar_musica(), self.resultado_esperado)

    def tearDown(self) -> None:
        print ('The End!')


if __name__=='__main__':
    unittest.main(verbosity=2)

    