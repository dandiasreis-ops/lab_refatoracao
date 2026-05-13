# CODE SMELLS ENCONTRADOS:
# Bloater - Classe Grande - responsabilidades demais para uma única classe
# Impedidores de Mudanças - Mudança Divergente - Se mudar banco de dados, XML, imposto, a mesma classe precisa ser alterada
# Bloater - Obsessão por tipos primitivos (SQL hardcoded) - SQL escrito diretamente na entidade
# Magic Number - valor sem contexto

# TÉCNICAS DE REFATORAÇÃO:
# Extrair Classes - aplicação de SRP
# Separar entidade, persistência e exportação
# Renomear Métodos, Variáveis e Classes
# Criação de Constante para remover o Magic Number


# CÓDIGO REFATORADO:

# CLASSE PRODUTO
class Produto:

    IMPOSTO = 0.15

    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_imposto(self):
        return self.preco * (1 + self.IMPOSTO)


# CLASSE RESPONSÁVEL PELO BANCO
class ProdutoRepository:

    def salvar(self, produto):

        print(
            f"INSERT INTO produtos "
            f"(id, nome, preco) "
            f"VALUES "
            f"({produto.id_produto}, "
            f"'{produto.nome}', "
            f"{produto.preco});"
        )


# CLASSE RESPONSÁVEL PELO XML
class ProdutoXMLExporter:

    def exportar(self, produto):

        return (
            f"<produto>"
            f"<id>{produto.id_produto}</id>"
            f"<nome>{produto.nome}</nome>"
            f"<preco>{produto.preco}</preco>"
            f"</produto>"
        )


# EXEMPLO DE USO

produto = Produto(1, "Notebook", 3500)

print(
    "Preço com imposto:",
    produto.calcular_preco_com_imposto()
)

repository = ProdutoRepository()
repository.salvar(produto)

exportador = ProdutoXMLExporter()
print(exportador.exportar(produto))