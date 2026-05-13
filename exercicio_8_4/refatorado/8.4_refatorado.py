# CODE SMELLS ENCONTRADOS:
# Abusadores de OO - Switch Statements - if-elif excessivo (falta de polimorfismo)
# Magic Numbers - Valores numéricos no código aparecem sem contexto

# TÉCNICAS DE REFATORAÇÃO:
# Substituir Condicional por Polimorfismos
# Extrair Classe
# Renomear Métodos, Variáveis e Classes


# CÓDIGO REFATORADO:

from abc import ABC, abstractmethod


# CLASSE ABSTRATA
class Transporte(ABC):

    @abstractmethod
    def calcular_frete(self, distancia):
        pass


# MOTO
class Moto(Transporte):

    VALOR_POR_KM = 2.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM


# CARRO
class Carro(Transporte):

    VALOR_POR_KM = 3.5
    TAXA_BASE = 10.0

    def calcular_frete(self, distancia):
        return (
            distancia * self.VALOR_POR_KM
            + self.TAXA_BASE
        )


# CAMINHÃO
class Caminhao(Transporte):

    VALOR_POR_KM = 8.0
    TAXA_BASE = 50.0

    def calcular_frete(self, distancia):
        return (
            distancia * self.VALOR_POR_KM
            + self.TAXA_BASE
        )


# BICICLETA
class Bicicleta(Transporte):

    VALOR_POR_KM = 1.0

    def calcular_frete(self, distancia):
        return distancia * self.VALOR_POR_KM


# EXEMPLO DE USO

moto = Moto()
print("Frete moto:", moto.calcular_frete(10))

carro = Carro()
print("Frete carro:", carro.calcular_frete(10))

caminhao = Caminhao()
print("Frete caminhão:", caminhao.calcular_frete(10))

bicicleta = Bicicleta()
print("Frete bicicleta:", bicicleta.calcular_frete(10))