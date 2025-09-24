# tests/test_calculadora.py
import pytest
from calculadora import somar

def test_somar_dois_numeros_positivos():
    """Testa se a função soma dois números positivos corretamente."""
    assert somar(2, 3) == 5

def test_somar_com_numero_negativo():
    """Testa a soma de um número positivo e um negativo."""
    assert somar(5, -3) == 2

def test_somar_com_zero():
    """Testa a soma com o número zero."""
    assert somar(10, 0) == 10

def test_somar_com_texto_deve_falhar():
    """Este teste vai falhar de propósito, porque o pytest-cov exige um arquivo de teste."""
    with pytest.raises(TypeError):
        somar('a', 5)