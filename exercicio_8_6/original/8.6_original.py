class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        # Verifica se o valor é maior que zero
        if valor > 0:
            # Adiciona a taxa do cartão de crédito (5%)
            valor_com_taxa = valor + (valor *0.05)
            # Imprime o valor na tela
            print(f"Processando crédito: R$ {valor_com_taxa}")
        else:
            # Retorna erro se for menor que zero
            print("Valor inválido")
    
    def processar_pagamento_debito(self, valor):
        # Verifica se o valor é maior que zero
        if valor > 0:
            # Adiciona a taxa do cartão de débito (2%)
            valor_com_taxa = valor + (valor * 0.02)
            # Imprime o valor na tela
            print(f"Processando débito: R$ {valor_com_taxa}")
        else:
            # Retorna erro se for menor que zero
            print("Valor inválido")