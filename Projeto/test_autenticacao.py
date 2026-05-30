from autenticacao import Autenticacao

def test_login_valido():
    auth = Autenticacao()
    auth.cadastrar_usuario("nycolle", "123456")

    assert auth.login("nycolle", "123456") == True

from autenticacao import Autenticacao
import pytest

def test_login_valido():
    auth = Autenticacao()
    auth.cadastrar_usuario("nycolle", "123456")

    assert auth.login("nycolle", "123456") == True

def test_usuario_duplicado():
    auth = Autenticacao()

    auth.cadastrar_usuario("nycolle", "123456")

    with pytest.raises(ValueError):
        auth.cadastrar_usuario("nycolle", "654321")
        

from autenticacao import Autenticacao
import pytest

def test_login_valido():
    auth = Autenticacao()
    auth.cadastrar_usuario("nycolle", "123456")

    assert auth.login("nycolle", "123456")

def test_usuario_duplicado():
    auth = Autenticacao()

    auth.cadastrar_usuario("nycolle", "123456")

    with pytest.raises(ValueError):
        auth.cadastrar_usuario("nycolle", "654321")

def test_senha_muito_curta():
    auth = Autenticacao()

    with pytest.raises(ValueError):
        auth.cadastrar_usuario("joao", "123")
        

def test_senha_incorreta():
    auth = Autenticacao()

    auth.cadastrar_usuario("nycolle", "123456")

    assert auth.login("nycolle", "000000") == False
    

def test_usuario_inexistente():
    auth = Autenticacao()

    assert auth.login("maria", "123456") == False

def test_redefinir_senha():
    auth = Autenticacao()

    auth.cadastrar_usuario("nycolle", "123456")

    auth.redefinir_senha("nycolle", "654321")

    assert auth.login("nycolle", "654321")