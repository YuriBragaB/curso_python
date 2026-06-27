import os
from supabase import create_client
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.security import APIKeyHeader
import requests
import jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

jwt_secret = os.getenv("JWT_KEY")
algoritmo = "HS256"

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)
api_key_correta = os.getenv("API_KEY")

app = FastAPI()
api_key_header = APIKeyHeader(name = 'api_key')
auth = OAuth2PasswordBearer(tokenUrl= "login")


# função para gerar o token
def criar_token(dados_usuarios):
    dados_token = dados_usuarios.copy()

    expiracao = datetime.now() + timedelta(minutes=30)

    dados_token.update({
        "exp" : expiracao
    })

    token = jwt.encode(dados_token, jwt_secret, algorithm = algoritmo)

    return token


@app.post('/login') 
def login(dados: dict = Body()):
    cpf = dados.get("cpf")
    senha = dados.get("senha")

    try:
        resposta = (supabase
                    .table("biblioteca_usuarios")
                    .select("nome, ativo, tipo")
                    .eq('cpf', cpf)
                    .execute())
        
        token = criar_token(resposta.data[0])

        return {
            "access_token" : token,
            "token_type" : 'bearer'
        }
    except Exception:
        HTTPException(status_code=401, detail='Chave API está errada')

def verificar_token(token: str = Depends(auth)):
    try:
        dados_token = jwt.decode(
            token,
            jwt_secret,
            algorithms = algoritmo
        )
    except Exception:
        pass

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