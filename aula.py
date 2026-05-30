# python-dotenv, é uma biblioteca para carregar variáveis de ambiente a partir de um arquivo .env
# é ótima para botar no .gitignore e não expor chaves de API, senhas, etc.
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv() 
# Carrega as variáveis de ambiente do arquivo .env

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase = create_client(supabase_url, supabase_key)

resposta = (supabase.table('pedidos')
            .select('id, preco, forma_pagamento')
            .eq('id_usuario', 2)
            .execute())

print(resposta.data)


# crie uma tabela chamada itens_pedidos, essa tabela deverá ter uma relação com a tabela pedidos, ou seja 1 pedido pode ter vários itens
# associados a eles, mas um item pedido só pode estar associado a um pedido, ou seja, uma relação de 1 para N. A tabela itens_pedidos deve ter os seguintes campos:
'''
itens_pedidos
nome
preco
quantidade
desconto
id_pedido (chave estrangeira para a tabela pedidos)

insira pelo menos 2 ou mais itens para cada pedido, ou seja, a ana fez o pedido um como os itens teclado, mouse e fone.

crie um código em python que busque no banco de dados todos os itens pedidos pelo usuário 2, trazendo: nome do usuário, valor do pedido, os items pedidos, o nome dos itens pedidos
'''
# tabela(tabela()) # pega de uma tabela e traz os dados de outra tabela relacionada a ela, ou seja, uma subconsulta
resposta = (supabase.table('itens_pedidos')
            .select('nome, pedidos(id, preco, usuários(nome))')
            .execute())
print(resposta.data)

resposta = (supabase.table('matricula')
            .select('alunos(nome), curso(nome)')
            .select('nome, pedidos(id, preco, usuários(nome))')
            .eq('id_aluno', 1)
            .execute())

for resp in resposta.data:
    print(f'{resp['alunos']} : {resp['curso']['nome']}:')