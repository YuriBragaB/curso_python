# git clone espaço ponto cria o clone em uma pasta nova
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

cep = int(input('Digite o seu CEP:\n'))
selecao = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}').json()
print(f'cidade : {selecao['city']}\nestado : {selecao['state']}\nnome da rua : {selecao['address']}')
