# CODE SMELLS ENCONTRADOS:
# Bloater - Lista longa de parâmetros - criar_reserva possui parâmetros demais
# Bloater - Obsessão por tipos primitivos - Muitos dados relacionados soltos, deveriam ser objetos/classes próprias
# Bloater - Método Longo - A função viola SRP
# Magic number - Esse eu pesquisei - valor fixo “mágico” no código-fonte sem explicação


# CÓDIGO REFATORADO:

from datetime import date


# CLASSE HÓSPEDE
class Hospede:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


# CLASSE QUARTO
class Quarto:
    def __init__(self, numero, tipo, valor_diaria):
        self.numero = numero
        self.tipo = tipo
        self.valor_diaria = valor_diaria


# CLASSE RESERVA
class Reserva:

    VALOR_CAFE_DA_MANHA = 50

    def __init__(
        self,
        hospede,
        quarto,
        data_checkin,
        data_checkout,
        possui_cafe_da_manha
    ):

        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    # CALCULAR TOTAL
    def calcular_total(self):

        total_dias = (self.data_checkout - self.data_checkin).days

        total = total_dias * self.quarto.valor_diaria

        if self.possui_cafe_da_manha:
            total += self.VALOR_CAFE_DA_MANHA * total_dias

        return total

    # EXIBIR RESERVA
    def exibir_reserva(self):

        print(
            f"Reserva criada para "
            f"{self.hospede.nome} "
            f"(CPF: {self.hospede.cpf})"
        )

        print(
            f"Quarto {self.quarto.numero} "
            f"({self.quarto.tipo})"
        )

        print(
            f"De {self.data_checkin} "
            f"até {self.data_checkout}"
        )

        print(f"Total a pagar: R$ {self.calcular_total()}")


# EXEMPLO DE USO

hospede = Hospede(
    "Bob",
    "12345678900",
    "bob@email.com"
)

quarto = Quarto(
    101,
    "Luxo",
    200
)

reserva = Reserva(
    hospede,
    quarto,
    date(2026, 5, 1),
    date(2026, 5, 5),
    True
)

reserva.exibir_reserva()