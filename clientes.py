from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def nova_ficha_de_cliente():

    Nome_do_Cliente = input("Introduzir nome do cliente: ")
    Novo_cliente_idade = int(input("Idade do cliente: "))

    while True:
        try:
            Novo_cliente_idade = int(input("Idade do cliente: "))
            if Novo_cliente_idade >= 18:
                break
            else:
                print("Desculpe, o cliente deve ter no mínimo 18 anos.")
        except ValueError:
            print("Forneça uma idade válida.")

    Novo_cliente_email = input("Email do cliente : ")

    while True:
        Numero_fiscal = input("Número fiscal do cliente (9 dígitos): ")
        if len(Numero_fiscal) == 9 and Numero_fiscal.isdigit():
            break
        else:

            dados_do_cliente = {"Nome": Nome_do_Cliente}, {"Idade" : Novo_cliente_idade}, {"Email" : Novo_cliente_email}, {"Número fiscal" :  Numero_fiscal}
    
    print(dados_do_cliente) 

nova_ficha_de_cliente()

