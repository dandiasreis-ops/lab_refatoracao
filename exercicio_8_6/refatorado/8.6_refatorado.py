# CODE SMELLS ENCONTRADOS:
# Descartáveis - Código Duplicado (Violação do DRY) - processar_pagamento_credito e processar_pagamento_debito possuem praticamente a mesma lógica
# Magic Numbers - valores sem contexto novamente
# Descartáveis - Comentários - Comentários excessivos ou óbvios

# TÉCNICAS DE REFATORAÇÃO:
# Extrair método comum para eliminar repetição (aplicação do DRY)
# Usar constantes e reduzir comentários


# CÓDIGO REFATORADO:

class ProcessadorFinanceiro:

    TAXA_CREDITO = 0.05
    TAXA_DEBITO = 0.02

    # MÉTODO GENÉRICO
    def processar_pagamento(self, valor, taxa, tipo_pagamento):

        # VALIDAR VALOR
        if valor <= 0:
            print("Valor inválido")
            return

        # CALCULAR TAXA
        valor_com_taxa = valor + (valor * taxa)

        # EXIBIR RESULTADO
        print(
            f"Processando {tipo_pagamento}: "
            f"R$ {valor_com_taxa}"
        )

    # CRÉDITO
    def processar_pagamento_credito(self, valor):

        self.processar_pagamento(
            valor,
            self.TAXA_CREDITO,
            "crédito"
        )

    # DÉBITO
    def processar_pagamento_debito(self, valor):

        self.processar_pagamento(
            valor,
            self.TAXA_DEBITO,
            "débito"
        )


# EXEMPLO DE USO

processador = ProcessadorFinanceiro()

processador.processar_pagamento_credito(100)

processador.processar_pagamento_debito(100)