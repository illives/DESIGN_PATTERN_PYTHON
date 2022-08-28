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
from Project.Ritimo_resource.Music_abstract import MusicRhythmSolid


class Test_MusicRhythm_Abstract(unittest.TestCase):
    def test_if_def_tocar_music_raise_notimplemented_error(self):
        radio = MusicRhythmSolid()
        with self.assertRaises(NotImplementedError):
            radio.tocar_musica()

            
if __name__ == "__main__":
    unittest.main(verbosity=2)





