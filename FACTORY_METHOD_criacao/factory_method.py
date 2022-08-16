"""
FACTORY METHOD é um pattern que permite definir uma interface (Classe abstrata) para criar objetos, mas deixas as subclasses (Classes que Herdam a classe abstrata) decidirem qual objeto irá criar.
Baixo Acomplamento
"""

from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: 
        pass

class Carro_Luxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de Luxo Buscando Cliente.')

class Carro_Popular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular Buscando Cliente.')

class Moto_Comun(Veiculo):
    def buscar_cliente(self):
        print('Moto Comun buscando Cliente.')

class Onibus_Comum(Veiculo):
    def buscar_cliente(self):
        print('Onibus buscando Cliente.')

class Veiculo_Factory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractclassmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class Zona_Norte_Factory_Veiculo(Veiculo_Factory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return Carro_Luxo()
        elif tipo == 'popular':
            return Carro_Popular()
        elif tipo == 'moto':
            return Moto_Comun()
        elif tipo == 'onibus':
            return Onibus_Comum()
        assert 0, 'Veiculo não existe'

class Zona_Sul_Factory_Veiculo(Veiculo_Factory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return Carro_Luxo()
        elif tipo == 'popular':
            return Carro_Popular()
        assert 0, 'Veiculo não existe'

if __name__=='__main__':
    from random import choice
    veiculos_disponiveis_znorte = ['luxo', 'popular', 'moto', 'onibus']
    veiculos_disponiveis_zsul = ['luxo', 'popular']

    print('ZONA NORTE')
    for req in range (10):
        carro = Zona_Sul_Factory_Veiculo(choice(veiculos_disponiveis_zsul))
        carro.buscar_cliente()

    print('ZONA SUL')
    for req in range (10):
        carro2 = Zona_Norte_Factory_Veiculo(choice(veiculos_disponiveis_znorte))
        carro2.buscar_cliente()
