import os
from supabase import create_client
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.security import APIKeyHeader
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)
api_key_correta = os.getenv("API_KEY")

app = FastAPI()
api_key_header = APIKeyHeader(name = 'api_key')

def verificar_api_key(api_key_recebida: str = Depends(api_key_header)):
    if api_key_recebida != api_key_correta:
        raise HTTPException(status_code=401, detail='Chave API está errada')
    return api_key_recebida

@app.get("/busca", api_keys = Depends(verificar_api_key))
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

# POST

@app.post("/livros")
def cadastrar_livro(dados: dict = Body()):
    resposta = (
                supabase
                .table("biblioteca_livro")
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

@app.post("/autor")
def cadastrar_autor(dados: dict = Body()):
    resposta = (
                supabase
                .table("biblioteca_autor")
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

@app.post("/livro")
def cadastrar_livro(dados: dict = Body()):
    resposta = (
                supabase
                .table("biblioteca_usuario")
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

@app.post("/perfil")
def cadastrar_perfil(dados: dict = Body()):
    resposta = (
                supabase
                .table("biblioteca_perfil")
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

@app.post("/emprestimo")
def cadastrar_emprestimo(dados: dict = Body()):
    resposta = (
                supabase
                .table("biblioteca_livro")
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

def cadastrar(tabela: str, dados: dict = Body()):
    resposta = (
                supabase
                .table(tabela)
                .insert(dados)
                .execute()
                )
    
    resposta = resposta.data
    return resposta

# DELETE
@app.delete("/deletarlivro/{id}")
def deletar_livro(id: int = None):
    resposta = (
                supabase
                .table("biblioeca_livro")
                .delete()
                .eq("id", id)
                .execute
                )
    
    return {
        "msg": "livro deletado com sucesso",
        }

# UPDATE / put
@app.put("/atualizarlivro/{id}")
def atualizar_livro(id: int, dados:dict = Body()):
    resposta = (
        supabase
        .table("biblioteca_livro")
        .update(dados)
        .eq('id', id)
        .execute()
    )

    return {
        "msg" : "livro atualizado com sucesso",
        "resposta" : resposta.data
    }