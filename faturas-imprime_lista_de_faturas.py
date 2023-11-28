def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""
    """
    Imprime os detalhes de cada fatura na lista.

    :param lista_de_faturas: Lista de dicionários representando faturas.
    """
    if not lista_de_faturas:
        print("Lista de faturas vazia.")
        return

    print("Detalhes das Faturas:")
    for index, fatura in enumerate(lista_de_faturas, start=1):
        print(f"--- Fatura {index} ---")
        print(f"Cliente: {fatura['cliente']}")
        print(f"Veículo: {fatura['veiculo']}")
        print(f"Data: {fatura['data']}")
        print(f"Valor Total: {fatura['valor_total']}")
        print(f"Descrição: {fatura['descricao']}")
        print("\n")

# Exemplo de uso
lista_de_faturas = [
    {"cliente": "1", "veiculo": "A123", "data": "2023-11-28", "valor_total": 1000.00, "descricao": "Serviços de manutenção"},
    {"cliente": "2", "veiculo": "B456", "data": "2023-11-29", "valor_total": 1500.00, "descricao": "Peças de reposição"},
    # Adicione mais faturas conforme necessário
]

imprime_lista_de_faturas(lista_de_faturas)