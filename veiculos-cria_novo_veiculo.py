def cria_novo_Perfil_de_utilizador():
    """pede ao utilizador para introduzir os seus dados e os dados do veiculo 
    
    :return: dicionario com um veiculo na forma {"marca": <<marca>>, "matricula": <<matricula>>, "cor": <<cor>>}
    """

    Morada_do_utilizador= input("intoduzir morada:")
    marca = input("marca do veiculo:")
    matricula = input ("Matricula do veiculo:").upper()
    cor= input("Cor do veicullo:")

    dados_do_veiculo = {"marca": marca},{"cor": cor},{"matricula":matricula}
    

    print(dados_do_veiculo)


cria_novo_Perfil_de_utilizador()
