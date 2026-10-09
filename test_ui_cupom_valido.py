
from playwright.sync_api import sync_playwright, expect


def test_interface_aplica_cupom_valido():
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

            expect(page.locator("li.item-carrinho")).to_be_visible()

            page.locator("#campo-cupom").fill("BEMVINDO10")
            page.locator(
                'form.cupom button[type="submit"]'
            ).click()

            expect(
                page.locator('dd[data-valor="subtotal"]')
            ).to_have_text("R$ 100,00")

            expect(
                page.locator('dd[data-valor="desconto"]')
            ).to_have_text("- R$ 10,00")

            expect(
                page.locator('dd[data-valor="total"]')
            ).to_have_text("R$ 109,90")

        finally:
            browser.close()