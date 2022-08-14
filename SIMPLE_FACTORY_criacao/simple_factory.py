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

class Veiculo_Factory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

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

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__=='__main__':
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto', 'onibus']

    for req in range (10):
        carro = Veiculo_Factory(choice(carros_disponiveis))
        carro.buscar_cliente()