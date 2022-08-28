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
from Project.Ritimo_resource.Rock_Rhythm import RockRythm

class TestRockRythim(unittest.TestCase):
    def setUp(self) -> None:
        self.radio = RockRythm()
        self.resultado = 'Tocando Musica de Rock'
    
    def test_if_function_tocar_musica_is_playing_rock(self):
        self.assertEqual(self.radio.tocar_musica(), self.resultado)

    def tearDown(self) -> None:
        print('The End!')


if __name__=='__main__':
    unittest.main(verbosity=2)