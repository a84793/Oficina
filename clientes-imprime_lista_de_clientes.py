def nova_ficha_de_cliente():
    """Criei uma função"""


    lista_de_clientes = []

    while True:
        Nome_do_Cliente = input("Introduzir nome do cliente: ")

        while True:
            try:
                Novo_cliente_idade = int(input("Idade do cliente: "))
                if Novo_cliente_idade >= 18:
                    break
                else:
                    print("Desculpe, o cliente deve ter no mínimo 18 anos.")
            except ValueError:
                print("Forneça uma idade válida.")

        Novo_cliente_email = input("Email do cliente: ")

        while True:
            Numero_fiscal = input("Número fiscal do cliente (9 dígitos): ")
            if len(Numero_fiscal) == 9 and Numero_fiscal.isdigit():
                break
            else:
                print("Número fiscal inválido. Deve conter 9 dígitos.")

        dados_do_cliente = {
            "Nome": Nome_do_Cliente,
            "Idade": Novo_cliente_idade,
            "Email": Novo_cliente_email,
            "Número fiscal": Numero_fiscal
        }

        lista_de_clientes.append(dados_do_cliente)

        adicionar_outro = input("Deseja adicionar outro cliente? (s/n): ").lower()
        if adicionar_outro != 's':
            break

    print("Lista de clientes:")
    for cliente in lista_de_clientes:
        print(cliente)

nova_ficha_de_cliente()