import pytest
import requests

# Criando a URL base
url_base = "http://127.0.0.1:8000"

# Teste de sucesso
def test_consultar_cnpj_success():
    # Utilizando um CNPJ válido seja usado para teste
    cnpj_valido = "27865757000102"
    
    response = requests.get(f"{url_base}/consultar-cnpj/{cnpj_valido}")
    assert response.status_code == 200
    json_response = response.json()
    assert "cnpj_raiz" in json_response


# Teste de erro: CNPJ inválido
def test_consultar_cnpj_invalid():
    # Suponha que um CNPJ inválido seja usado para teste
    cnpj_invalido = "cnpj_invalido"
    
    response = requests.get(f"{url_base}/consultar-cnpj/{cnpj_invalido}")
    assert response.status_code == 404
    json_response = response.json()
    assert "detail" in response.json()
    assert response.json()["detail"] == "Erro na consulta do CNPJ"


# Teste de erro: resposta não foi bem sucedida
def test_consultar_cnpj_error():
    # Suponha que a consulta retorne um código de status diferente de 200
    cnpj_errado = "12345678901234"

    response = requests.get(f"{url_base}/consultar-cnpj/{cnpj_errado}")
    assert response.status_code == 400
    json_response = response.json()
    assert "detail" in response.json()
    assert response.json()["detail"] == "Erro na consulta do CNPJ"