def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
    """função que guarda as listas nos ficheiros

    :param lista_de_clientes: Guarda os dados da lista de clientes e coloca no ficheiro
    :param lista_de_veiculos: Guarda os dados da lista de clientes e colocar no ficheiro
    :param lista_de_faturas: Guarda os dados da lista de clientes e colocar no ficheiro
    """

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")
