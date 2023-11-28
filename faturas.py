from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

         # Solicitar ao usuário para inserir os dados da fatura
    id_cliente = input("Digite o ID do cliente: ")
    id_veiculo = input("Digite o ID do veículo: ")
    data = input("Digite a data da fatura (formato YYYY-MM-DD): ")
    valor_total = float(input("Digite o valor total da fatura: "))
    descricao = input("Digite uma breve descrição da fatura: ")

    # Criar e retornar o dicionário com os dados da fatura
    fatura = {
        "cliente": id_cliente,
        "veiculo": id_veiculo,
        "data": data,
        "valor_total": valor_total,
        "descricao": descricao
    }

 # Exemplo de uso
    nova_fatura = obter_dados_fatura()
    print("Fatura inserida:")
    print(nova_fatura)

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today()}

    return fatura

def imprime_lista_de_faturas(lista_de_faturas):

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