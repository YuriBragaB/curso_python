'''
EXERCÍCIO — MODELAGEM DE BANCO DE DADOS NO SUPABASE

Um cliente contratou vocês para desenvolver o banco de dados inicial de um sistema bancário digital simples.

O sistema precisa registrar:

* clientes do banco
* contas bancárias
* transações financeiras
* serviços oferecidos pelo banco
* contratação de serviços pelos clientes

Todas as tabelas devem seguir o padrão:

nomedobanco_nomedatabela

Exemplo:

banco_clientes

banco_transacoes

REQUISITOS DO SISTEMA

1. Clientes

O sistema precisa armazenar os dados dos clientes.

Informações principais:

* nome
* cpf
* email
* telefone
* data de cadastro
* status ativo/inativo

2. Contas bancárias

O sistema precisa armazenar os dados das contas bancárias dos clientes.

Informações principais:

* número da conta
* agência
* tipo da conta
* data de abertura
* saldo inicial

3. Transações

O sistema precisa registrar as movimentações financeiras realizadas pelos clientes.

Informações principais:

* tipo da transação
* valor
* data da transação
* descrição

4. Serviços bancários

O banco oferece alguns serviços extras aos clientes.

Exemplos:

* cartão de crédito
* seguro
* empréstimo
* investimento

Informações principais:

* nome do serviço
* descrição
* taxa mensal
* status ativo/inativo

5. Contratação de serviços

O sistema também precisa registrar quais clientes contrataram quais serviços.

Informações principais:

* data da contratação
* status
* observação

REGRAS

* Todas as tabelas devem possuir chave primária.
* Escolham corretamente os tipos de dados.
* Criem os relacionamentos necessários entre as tabelas.
* Identifiquem corretamente quais campos devem ser chave estrangeira.
* Pensem cuidadosamente no tipo de relacionamento existente entre as entidades.

O objetivo NÃO é apenas criar tabelas isoladas.

O banco deve representar corretamente a relação entre os dados do sistema.
'''
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)


def exibir_resposta(resposta : dict) -> None:
    for dic in (resposta := resposta.data): # .data retorna um dic com listas dentro
        for coluna, resp in dic.items():
            print(f'{coluna} : {resp}')
        print('-'* 50)

# relacionamento entre as tabelas:
    '''
    2 - 1 = 1:1
    3 - 2 = n:1
    4 - 3 = n:n
    5 - 4 = 1:n
    '''

# UPDATE:
def atualizar_dados(tabela : str, id : int, dados : dict) -> None:
    try:
        resposta = supabase.table(tabela).update(dados).eq('id',id).execute()
        print('Dados atualizados com sucesso')
    except Exception as erro: # Exception é a classe pai de quase todos os erros padrão
        print(f'Erro ao atualizar os dados: {erro}')  
 
def coletar_dados_e_atualizar():
    print('Selecione a tabela que você deseja inserir:\n')
    tabelas = {
        1 : 'banco_cliente',
        2 : 'banco_contas_bancarias',
        3 : 'banco_transacoes',
        4 : 'banco_servicos_bancarios',
        5 : 'banco_contratacao_de_servicos'
    }
    campos_tabela = {
        'banco_cliente' : ['id', 'nome', 'cpf', 'email', 'status' ],
        'banco_contas_bancarias' : ['id', 'numero_da_conta', 'agencia', 'tipo_da_conta', 'data_de_abertura', 'saldo_inicial', 'cliente_id'],
        'banco_transacoes' : ['id', 'tipo_da_transacao', 'data_da_trasacao', 'descricao', 'contas_bancarias_id'],
        'banco_servicos_bancarios' : ['id', 'nome_do_servico', 'descricao', 'taxa_mensal', 'status', 'transacoes_id'],
        'banco_contratacao_de_servicos' : ['id', 'status', 'observacao', 'data_da_contratacao', 'servicos_bancarios_id']
    }

    for chave, valor in tabelas.items():
        print(f'{chave} : {valor}')

    tabela = int(input('\nDigite o número da tabela:\n'))
    while tabela not in [1, 2, 3, 4, 5]:
        os.system('cls')
        print('Digite um número válido!\n')

        for chave, valor in tabelas.items():
            print(f'{chave} : {valor}')

        tabela = int(input('\nDigite o número da tabela:\n'))

    tabela_selecionada = tabelas[tabela]
    resposta = (supabase.table(tabela_selecionada)
                .select('*')
                .execute())
    os.system('cls')

    print(f'\nA tabela selecionada foi: {tabela_selecionada}\n')
    
    print('-' * 50)
    exibir_resposta(resposta)

    id = int(input('\nDigite o ID que você deseja alterar:\n'))

    resposta = supabase.table(tabela_selecionada).select('*').eq('id', id).execute()
    aux = resposta.data[0] # pega o primeiro registro
    novos_dados = {}

    for campo in campos_tabela[tabela_selecionada]:
        print(f'{campo} : {aux[campo]}')
        novos_dados[campo] = input(f'Novo valor:\n')
        os.system('cls')
    
    atualizar_dados(tabela_selecionada, id, novos_dados)



# DELETE
def deletar_dados(tabela : str, id : int) -> None:
    try:
        resposta = supabase.table(tabela).delete().eq('id',id).execute()
        print('Dados deletados')
    except Exception as erro: # excepition é a classe pai de diversos erros em python
        print(f'Erro ao deletar os dados: {erro}')

def coletar_dados_e_deletar():
    print('Selecione a tabela que você deseja deletar:\n')
    tabelas = {
        1 : 'banco_cliente',
        2 : 'banco_contas_bancarias',
        3 : 'banco_transacoes',
        4 : 'banco_servicos_bancarios',
        5 : 'banco_contratacao_de_servicos'
    }
    
    for chave, valor in tabelas.items():
        print(f'{chave} : {valor}')

    tabela = int(input('\nDigite o número da tabela:\n'))
    while tabela not in [1, 2, 3, 4, 5]:
        os.system('cls')
        print('Digite um número válido!\n')

        for chave, valor in tabelas.items():
            print(f'{chave} : {valor}')

        tabela = int(input('\nDigite o número da tabela:\n'))

    os.system('cls')

    tabela_selecionada = tabelas[tabela]
    resposta = (supabase
                .table(tabela_selecionada)
                .select('*')
                .execute())
    
    print('-' * 50)
    exibir_resposta(resposta)

    id = int(input('\nDigite o id da linha que você deseja deletar:\n'))
    
    deletar_dados(tabela_selecionada, id)

coletar_dados_e_deletar()