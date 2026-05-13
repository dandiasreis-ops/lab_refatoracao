# CODE SMELLS ENCONTRADOS:
# Bloater - Método Longo (Long Method) - processar_venda_e_gerar_relatorio() - responsabilidades demais no mesmo método
# Bloater - Classe Grande - GerenciadorDeVendas - viola SRP (Single Responsibility Principle)
# Abusadores de OO - Switch Statements - if excessivo

# CÓDIGO REFATORADO:

# CLASSE RESPONSÁVEL PELO RELATÓRIO
class RelatorioVendas:
    def gerar(self, cliente, total):
        relatorio = (
            f"--- Relatório de Venda ---\n"
            f"Cliente: {cliente['nome']}\n"
            f"Total: R$ {total}\n"
        )

        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)

        print("Relatório gerado com sucesso.")


# CLASSE RESPONSÁVEL PELO PAGAMENTO
class ProcessadorPagamento:
    def processar(self, metodo_pagamento, total):

        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")

        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

        else:
            print("Método de pagamento inválido.")


# CLASSE PRINCIPAL DE VENDAS
class GerenciadorDeVendas:

    # CALCULAR TOTAL DA VENDA
    def calcular_total(self, itens):
        total = 0

        for item in itens:
            total += item['preço'] * item['quantidade']

        return total

    # APLICAR DESCONTO
    def aplicar_desconto(self, cliente, total):

        if cliente['tipo'] == 'VIP':
            total *= 0.90

        return total

    # PROCESSAR VENDA
    def processar_venda(self, itens, cliente, metodo_pagamento):

        # cálculo
        total = self.calcular_total(itens)

        # desconto
        total = self.aplicar_desconto(cliente, total)

        # pagamento
        pagamento = ProcessadorPagamento()
        pagamento.processar(metodo_pagamento, total)

        # relatório
        relatorio = RelatorioVendas()
        relatorio.gerar(cliente, total)

        print("Venda processada com sucesso.")