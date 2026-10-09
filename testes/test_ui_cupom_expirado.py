
from playwright.sync_api import sync_playwright, expect


def test_interface_rejeita_cupom_expirado():
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

            page.locator("#campo-cupom").fill("VERAO2026")
            page.locator(
                'form.cupom button[type="submit"]'
            ).click()

            expect(
                page.get_by_text("Cupom expirado.", exact=True)
            ).to_be_visible()

            expect(
                page.locator('dd[data-valor="desconto"]')
            ).to_have_text("R$ 0,00")

        finally:
            browser.close()
