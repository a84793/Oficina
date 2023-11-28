from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):

    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

       
    id_cliente = input("Digite o ID do cliente: ")
    id_veiculo = input("Digite o ID do veículo: ")
    data = input("Digite a data da fatura (formato YYYY-MM-DD): ")
    valor = float(input("Digite o valor total da fatura: "))

    fatura = {"cliente": id_cliente,
              "veiculo": id_veiculo,
              "data": date.today(),
                "valor": valor,
                "data": data}

    return fatura

def imprime_lista_de_faturas(lista_de_faturas):

    imprime_lista(cabeçalho="lista de faturas", lista = lista_de_faturas)