
from playwright.sync_api import sync_playwright


def test_frete_gratis_com_subtotal_de_200():
    with sync_playwright() as playwright:
        request = playwright.request.new_context(
            base_url="https://verzel-store.qa-test-verzel-store.workers.dev"
        )

        response = request.post(
            "/api/carrinho/calcular",
            data={
                "itens": [{"produtoId": "P008", "quantidade": 4}],
                "cupom": "BEMVINDO10",
            },
        )

        assert response.status == 200

        resultado = response.json()
        assert resultado["subtotal"] == 200
        assert resultado["desconto"] == 20
        assert resultado["frete"] == 0
        assert resultado["freteGratis"] is True
        assert resultado["valorFaltanteFreteGratis"] == 0
        assert resultado["total"] == 180

        request.dispose()