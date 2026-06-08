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

# tabelas estão feitas no supabase, falta fazer o relacionamento entre elas