from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_Perfil_de_utilizador():
    
    Morada_do_utilizador= input("intoduzir morada:")
    marca = input("marca do veiculo:")
    matricula = input ("Matricula do veiculo:").upper()
    cor= input("Cor do veicullo:")

    dados_do_veiculo = {"marca": marca},{"cor": cor},{"matricula":matricula}
    

    print(dados_do_veiculo)


cria_novo_Perfil_de_utilizador()
