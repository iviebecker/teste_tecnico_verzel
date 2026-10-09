
from playwright.sync_api import sync_playwright


def test_cupom_expirado_nao_aplica_desconto():
    with sync_playwright() as playwright:
        request = playwright.request.new_context(
            base_url="https://verzel-store.qa-test-verzel-store.workers.dev"
        )

        response = request.post(
            "/api/carrinho/calcular",
            data={
                "itens": [{"produtoId": "P005", "quantidade": 1}],
                "cupom": "VERAO2026",
            },
        )

        assert response.status == 200

        resultado = response.json()
        assert resultado["subtotal"] == 100
        assert resultado["desconto"] == 0
        assert resultado["frete"] == 19.9
        assert resultado["total"] == 119.9
        assert resultado["cupom"]["aplicado"] is False
        assert resultado["cupom"]["mensagem"] == "Cupom expirado."

        request.dispose()