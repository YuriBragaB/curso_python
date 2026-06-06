import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL') 
supabase_key = os.getenv('SUPABASE_KEY') 
supabase = create_client(supabase_url, supabase_key)


def mensagem(dado):
    for pergunta, resposta in dado.items():
        print(f'{pergunta} : {resposta}')

# CRUD

def inserir_usuario():
    nome = input('Digite o nome:\n')
    cpf = input('Digite o cpf:\n')
    telefone = input('Digite o telefone:\n')
    endereco = input('Digite o endereço:\n')

    novo_usuario ={
        'nome' : nome,
        'cpf' : cpf,
        'telefone' : telefone,
        'endereço' : endereco
    }
    resposta = (supabase.table('biblioteca_usuario')
                .insert(novo_usuario)
                .execute())
    os.system('cls')
    (mensagem(novo_usuario))

def inserir_dados_tabela(tabela, dados):
    try:
        resposta = (supabase.table(tabela)
                    .insert(dados)
                    .execute())
        
        print('Dados inseridos com sucesso')
    except Exception as erro:
        print(f'Erro ao inserir os dados: {erro}')

def coletar_dados_e_inserir():
    opcao = int(input(('Selecione uma opção:\n'
    '1 | Inserir usuário\n'
    '2 | Inserir perfil\n'
    '3 | Inserir autor\n'
    '4 | Inserir autor\n'
    '5 | Inserir empréstimos\n')))

    if opcao == 1:
        tabela = 'biblioteca_usuario'

        nome = input('Digite o nome:\n')
        cpf = input('Digite o cpf:\n')
        telefone = input('Digite o telefone:\n')
        endereco = input('Digite o endereço:\n')

        novo_usuario = {
            'nome' : nome,
            'cpf' : cpf,
            'telefone' : telefone,
            'endereço' : endereco
        }

        inserir_dados_tabela(tabela, novo_usuario)
    elif opcao == 2:
        tabela = 'biblioteca_perfil'

        foto = input('Digite a url da foto:\n')
        bio = input('Digite a bio:\n')
        preferencias = input('Digite as suas preferências:\n')
        id_usuario = input('Digite o id do usuário:\n')

        novo_perfil = {
            'foto' : foto,
            'bio' : bio,
            'preferencias' : preferencias,
            'id_usuario' : id_usuario
        }

        inserir_dados_tabela(tabela, novo_perfil)

    elif opcao == 3:
        tabela = 'biblioteca_autor'
        
        nome = input('Digite o nome:\n')
        genero = input('Digite o gênero textual:\n')
        nacionalidade = input('Digite a sua nacionalidade:\n')


        novo_autor = {
            'nacionalidade' : nacionalidade,
            'genero' : genero,
            'nome' : nome,
        }

        inserir_dados_tabela(tabela, novo_autor)

    elif opcao == 4:
        tabela = 'biblioteca_livro'

        titulo = input('Digite o nome do livro:\n')
        quantidade = input('Digite a quantidade de livros:\n')
        genero = input('Digite o gênero textual:\n')
        ano = input('Digite o ano:\n')
        id_autor = input('Digite o ID do autor:\n')


        novo_livro = {
            'titulo' : titulo,
            'quantidade' : quantidade,
            'genero' : genero,
            'ano' : ano,
            'id_autor' : id_autor,
        }

        inserir_dados_tabela(tabela, novo_livro)

    elif opcao == 5:
        tabela = 'biblioteca_emprestimos'

        id_livro = input('Digite o ID do livro:\n')
        id_usuario = input('Digite o ID do usuário:\n')
        data_entrega = input('Digite a data de entrega:\n')

        novo_emprestimo = {
            'id_livro' : id_livro,
            'id_usuario' : id_usuario,
            'data_entrega' : data_entrega,
        }

        inserir_dados_tabela(tabela, novo_emprestimo)

# UPDATE

def atualizar_dados(tabela,id,dados):
    try:
        resposta = supabase.table(tabela).update(dados).eq('id',id).execute()
        print('Dados atualizados com sucesso')
    except Exception as erro:
        print(f'Erro ao atualizar os dados: {erro}')

def coletar_dados():
    print('Qual tabela você quer atualizar?')
    tabelas = {
        "1":"biblioteca_usuario",
        "2":"biblioteca_perfil",
        "3":"biblioteca_autor",
        "4":"biblioteca_livro",
        "5":"biblioteca_emprestimo"
    }
    campos_tabela = {
        "biblioteca_usuarios" : ["nome","cpf","endereco","ativo", "telefone"],
        "biblioteca_perfil" : ["foto",'bio','preferencias'],
        "biblioteca_autor" : ["nome","genero","nacionalidade"],
        "biblioteca_livro" : ["titulo","quantidade","genero","ano"],
        "emprestimo" : ["data_devolucao"]
    }

    for chave, valor in tabelas.items():
        print(f'{chave} - {valor}')

    opcao = input('Digite a opcao desejada: ')
    tabela_selecionada = tabelas[opcao]
    resposta = supabase.table(tabela_selecionada).select('*').execute()

    print('Selecione o ID que você quer atualizar')

    for resposta in resposta.data:
        print("################################")
        for chave, valor in resposta.items():
            print(f'{chave} - {valor}')
    id = input('Digite o ID que você quer atualizar: ')

    resposta = supabase.table(tabela_selecionada).select('*').eq('id', id).execute()
    novos_dados = {}

    for campo in campos_tabela[tabela_selecionada]:
        print(f'Valor atual do {campo} = {resposta[campo]}')
        novos_dados[campo] = input(f'Novo valor = ')

    atualizar_dados(tabela_selecionada, id, novos_dados)

#DELETE
def deletar_dados(tabela, id):
    try:
        resposta = supabase.table(tabela).delete().eq('id',id).execute()
        print('Dados deletados')
    except Exception as erro:
        print(f'Erro ao deletar os dados: {erro}')

def coletar_dados_deletar():
    print('De qual tabela você quer deletar?')
    tabelas = {
        "1":"biblioteca_usuario",
        "2":"biblioteca_perfil",
        "3":"biblioteca_autor",
        "4":"biblioteca_livro",
        "5":"biblioteca_emprestimo"
    }
    
    for chave, valor in tabelas.items():
        print(f'{chave} - {valor}')

    opcao = input('Digite a tabela: ')
    tabela_selecionada = tabelas[opcao]
    resposta = supabase.table(tabela_selecionada).select('*').execute()

    print('Selecione o ID que voce quer deletar')
    for resposta in resposta.data:
        print("################################")
        for chave, valor in resposta.items():
            print(f'{chave} - {valor}')
    id = input('Digite o ID que você quer atualizar: ')

    resposta = supabase.table(tabela_selecionada).select('*').eq('id', id).execute()