
from Project.Ritimo_resource.Evangelico_Rhythm import EvangelicoRythm
from Project.Ritimo_resource.Rock_Rhythm import RockRythm
from Project.Ritimo_resource.Music_Factory import MusicFactory

class RegionOneMusic(MusicFactory):
    
    @staticmethod
    def select_radio(rythm: str):
        if rythm == 'evangelico':
            return EvangelicoRythm()
        elif rythm == 'rock':
            return RockRythm()



