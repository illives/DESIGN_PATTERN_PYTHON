from abc import ABC, abstractclassmethod

class MusicRhythmAbstract(ABC):

    @abstractclassmethod
    def tocar_musica(self) -> None:
        raise NotImplementedError

class MusicRhythmSolid(MusicRhythmAbstract):
    def tocar_musica(self) -> None:
        raise NotImplementedError
