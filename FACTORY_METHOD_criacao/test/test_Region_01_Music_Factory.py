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
from Project.Ritimo_resource.Region_01__Music_Factory import RegionOneMusic


class TestRegionOneMusic(unittest.TestCase):
    def setUp(self):
        self.rythm = ['evangelico', 'rock']
    
    def test_if_select_radio_return_rock(self):
        radio = RegionOneMusic(self.rythm[1])
        self.assertEqual(radio.tocar_musica(), None)
    
    def tearDown(self):
        print('Fim do teste')


if __name__=='__main__':
    unittest.main(verbosity=2)