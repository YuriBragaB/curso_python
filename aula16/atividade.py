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

# Verifique no seu supabase se você ja tem o banco de dados do sistema financeiro que desenvolvemos em sala.
# Crie 4 APIs para o sistema financeiro:

# 1 Listar os usuário
# 2 Cadastrar uma transação 
# 3 Listar todas as transações de um usuário por meio do ID
# 4 Atualizar os dados de um usuário

# Crie uma chave de API para autenticar os acessos a essas 4 APIs
