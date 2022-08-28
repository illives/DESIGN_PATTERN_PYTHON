
from abc import ABC, abstractclassmethod


class MusicFactory(ABC):
    def __init__(self, rythm: str):
        self.radio = self.select_radio(rythm)
    
    @staticmethod
    @abstractclassmethod
    def select_radio(rythm: str):
        pass

    def tocar_musica(self):
        self.radio.tocar_musica()

