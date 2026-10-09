
from playwright.sync_api import sync_playwright, expect


def test_interface_limita_quantidade_maxima_a_cinco():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        try:
            page.goto(
                "https://verzel-store.qa-test-verzel-store.workers.dev"
            )

            produto = page.locator("li.produto").filter(
                has_text="Mochila Urbana 20L"
            )
            produto.get_by_role(
                "button", name="Adicionar ao carrinho"
            ).click()

            page.get_by_role("link", name="Carrinho").click()

            aumentar = page.get_by_role(
                "button",
                name="Aumentar quantidade de Mochila Urbana 20L"
            )

            quantidade = page.locator(
                'output[aria-label="Quantidade de Mochila Urbana 20L"]'
            )

            for _ in range(4):
                aumentar.click()

            expect(quantidade).to_have_text("5")

            expect(aumentar).to_be_disabled()
            expect(quantidade).to_have_text("5")

        finally:
            browser.close()
