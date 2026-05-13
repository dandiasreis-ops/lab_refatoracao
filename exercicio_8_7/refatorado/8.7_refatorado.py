# CODE SMELLS ENCONTRADOS:
# Acoplador - Message Chains (Correntes de Mensagens) - Sequência muito longa de chamados a métodos - navegação profunda entre objetos
# Acoplador - Intimidade Inapropriada (ou a Law of Demeter) - A função conhece detalhes internos demais da estrutura dos objetos
# A lógica de descobrir o país deveria estar encapsulada

# TÉCNICAS DE REFATORAÇÃO:
# Remoção do message chain
# Encapsulamento do acesso ao país dentro das próprias classes - esconder a cadeia


# CÓDIGO REFATORADO:

# CLASSE PAÍS
class Pais:

    def __init__(self, nome):
        self.nome = nome


# CLASSE ESTADO
class Estado:

    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    def obter_nome_pais(self):
        return self.pais.nome


# CLASSE ENDEREÇO
class Endereco:

    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

    def obter_nome_pais(self):
        return self.estado.obter_nome_pais()


# CLASSE CLIENTE
class Cliente:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def obter_nome_pais(self):
        return self.endereco.obter_nome_pais()


# CLASSE PEDIDO
class Pedido:

    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def obter_nome_pais(self):
        return self.cliente.obter_nome_pais()


# FUNÇÃO REFATORADA
def verificar_frete_internacional(pedido):

    pais_destino = pedido.obter_nome_pais()

    if pais_destino != "Brasil":
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão")


# EXEMPLO DE USO

pais = Pais("Brasil")

estado = Estado("São Paulo", pais)

endereco = Endereco("Rua A", estado)

cliente = Cliente("Bob", endereco)

pedido = Pedido(cliente, 500)

verificar_frete_internacional(pedido)