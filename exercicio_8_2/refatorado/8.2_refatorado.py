# CODE SMELLS ENCONTRADOS:
# Bloater - Lista longa de parâmetros - O construtor possui parâmetros demais
# Bloater - Obsessão por tipos primitivos - Muitos dados relacionados soltos, deveriam virar objetos/classes próprias
# Bloater - Classe Grande - Funcionario guarda muitos dados - melhor separar responsabilidades

# TÉCNICAS DE REFATORAÇÃO:
# Extrair Classes
# Remoção de lista longa de parâmetros
# Melhorar modelagem OO - cada classe representa uma entidade lógica


# CÓDIGO REFATORADO:

# CLASSE ENDEREÇO
class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def exibir(self):
        return (
            f"{self.rua}, {self.numero} - "
            f"{self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"
        )


# CLASSE TELEFONE
class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def exibir(self):
        return f"({self.ddd}) {self.numero}"


# CLASSE FUNCIONÁRIO
class Funcionario:
    def __init__(self, nome, cargo, salario, endereco, telefone):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone

    def exibir_dados(self):
        print(f"Funcionário: {self.nome} - {self.cargo}")
        print(f"Contato: {self.telefone.exibir()}")
        print(f"Endereço: {self.endereco.exibir()}")


# EXEMPLO DE USO

endereco = Endereco(
    "Rua A",
    123,
    "Centro",
    "São Paulo",
    "SP",
    "00000-000"
)

telefone = Telefone("11", "99999-9999")

funcionario = Funcionario(
    "Bob",
    "Desenvolvedor",
    5000,
    endereco,
    telefone
)

funcionario.exibir_dados()