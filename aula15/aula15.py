import os
from supabase import create_client
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

app = FastAPI()

# Query strings, são strings de pesquisa

@app.get("/busca")
def busca(titulo: str = None, quantidade: int = None, genero: str = None, ano: int = None):

    resposta = (supabase
                .table('biblioteca_livro')
                .select("*"))
    
    if titulo:
        resposta = resposta.ilike("titulo", f'%{titulo}%')

    if quantidade:
        resposta = resposta.eq("quantidade", quantidade)

    if genero:
        resposta = resposta.ilike("genero", f"{genero}")
        
    if ano:
        resposta = resposta.eq("ano", ano)

    livros = resposta.execute()
    if len(livros) == 0:
        return {"Mensagem: Livro não encontrado"}
    
    return livros

