from a1_modelo_simples import Pessoa, pessoas_interno

# esta função retorna a lista de pessoas
# em um formato a ser exibido pela tabela do streamlit
# está armazenada na lista interna
def retornar_pessoas_formato_tabela():   

    # converte a lista de objetos para um formato
    # que o streamlit consegue mostrar
    nomes = []
    emails = []
    telefones = []
    
    for p in pessoas_interno:
        nomes.append(p.nome)
        emails.append(p.email)
        telefones.append(p.telefone)
    
            # formata os dados para mostrar na camada de visão
    dados_no_formato = {
        "Nome": nomes,
        "Email": emails,
        "Telefone": telefones
    }

    # retorna os dados
    return dados_no_formato

# esta função insere uma pessoa
def inserir_pessoa(nome : str, email : str, telefone : str):
    
    # cria uma pessoa
    nova = Pessoa(nome, email, telefone)
    
    # adiciona no cadastro interno
    pessoas_interno.append(nova)    