from Project.Ritimo_resource.Music_abstract import MusicRhythmAbstract


class RockRythm(MusicRhythmAbstract):

    def tocar_musica(self) -> None:
        print('Selecionando Musica de Rock')
        return 'Tocando Musica de Rock'
