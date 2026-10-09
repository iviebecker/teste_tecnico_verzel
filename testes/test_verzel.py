
import pytest
from playwright.sync_api import sync_playwright

URL = "https://verzel-store.qa-test-verzel-store.workers.dev"


@pytest.fixture
def api():
    with sync_playwright() as p:
        request = p.request.new_context(
            base_url=URL,
            extra_http_headers={
                "Content-Type": "application/json"
            },
        )
        yield request
        request.dispose()


def test_cupom_valido_aplica_10_por_cento(api):
    response = api.post(
        "/api/carrinho/calcular",
        data={
            "itens": [{"produtoId": "P005", "quantidade": 1}],
            "cupom": "BEMVINDO10",
        },
    )

    assert response.status == 200
    data = response.json()
    assert data["subtotal"] == 100
    assert data["desconto"] == 10
    assert data["frete"] == 19.9
    assert data["total"] == 109.9
    assert data["cupom"]["aplicado"] is True


def test_frete_gratis_com_subtotal_exato_de_200(api):
    response = api.post(
        "/api/carrinho/calcular",
        data={
            "itens": [{"produtoId": "P008", "quantidade": 4}],
            "cupom": "BEMVINDO10",
        },
    )

    assert response.status == 200
    data = response.json()
    assert data["subtotal"] == 200
    assert data["desconto"] == 20
    assert data["frete"] == 0
    assert data["freteGratis"] is True
    assert data["total"] == 180


def test_cupom_expirado_nao_aplica_desconto(api):
    response = api.post(
        "/api/carrinho/calcular",
        data={
            "itens": [{"produtoId": "P005", "quantidade": 1}],
            "cupom": "VERAO2026",
        },
    )

    assert response.status == 200
    data = response.json()
    assert data["desconto"] == 0
    assert data["cupom"]["aplicado"] is False
    assert data["cupom"]["mensagem"] == "Cupom expirado."
    assert data["total"] == 119.9


def test_quantidade_acima_de_5_e_rejeitada(api):
    response = api.post(
        "/api/carrinho/calcular",
        data={
            "itens": [{"produtoId": "P008", "quantidade": 6}],
        },
    )

    assert response.status == 422
    data = response.json()
    assert data["erro"]["codigo"] == "QUANTIDADE_MAXIMA_EXCEDIDA"
