# git clone espaço ponto cria o clone em uma pasta nova
# executar o fastapi com o univorn(servidor que a gnt vai criar)
# uvicorn aula14:app --reload
import os
from supabase import create_client
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)
#CRUD

# selecao = int(input('Digite o id do produto que você quer utilizar'))
# produtos = requests.get(f'https://fakestoreapi.com/products/{selecao}').json() # pega a API 
# print(produtos)

# cep = int(input('Digite o seu CEP:\n'))
# selecao = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}').json()
# print(f'cidade : {selecao['city']}\nestado : {selecao['state']}\nnome da rua : {selecao['address']}')


app = FastAPI()

# criação das primeiras rotas da API
@app.get('/usuarios')
def get_usuario():
    resposta = supabase.table('biblioteca_usuario').select('*').execute()
    usuarios = resposta.data
    return usuarios
    # return {'mensagem' : 'API da biblioteca funcionando!'} # arquivos de API sempre são em JSON, por isso as chaves
    
# @app.get('/usuarios/{id}')
# def get_usuario_id(id : int):
#     resposta = (supabase
#                 .table('biblioteca_usuario')
#                 .select('*')
#                 .eq('id', id)
#                 .execute())

#     usuarios = resposta.data
    
#     if len(usuarios) == 0:
#         return {"mensagem: usuario não encontrado"}
    
#     return usuarios

@app.get('/usuarios/{cpf}')
def get_usuario_cpf(cpf : int):
    resposta = (supabase
                .table('biblioteca_usuario')
                .select('*')
                .eq('cpf', cpf)
                .execute())

    usuarios = resposta.data
    
    if len(usuarios) == 0:
        return {"mensagem: usuario não encontrado"}
    
    return usuarios

