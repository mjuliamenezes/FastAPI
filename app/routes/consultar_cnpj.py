from fastapi import APIRouter, HTTPException
import requests
from typing import Dict

router = APIRouter()

# Rota para consultar CNPJ
@router.get("/consultar-cnpj/{cnpj}")
def consultar_cnpj(cnpj: str):
    # Remove qualquer caractere não numérico do CNPJ
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Construe a URL da API do CNPJ.WS
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

    # Faz a requisição para a API do CNPJ.WS
    response = requests.get(url)

    # Verifica o código de status da resposta
    if response.status_code == 200:
        # Se a resposta foi bem-sucedida, retorna os dados do CNPJ
        return response.json()
    else:
        # Se a resposta não foi bem-sucedida, levanta uma exceção HTTP
        raise HTTPException(status_code=response.status_code, detail="Erro na consulta do CNPJ")