
from playwright.sync_api import sync_playwright, expect


def test_fluxo_carrinho_ate_checkout():
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
            aumentar.click()

            expect(
                page.locator('dd[data-valor="subtotal"]')
            ).to_have_text("R$ 200,00")

            expect(
                page.locator('dd[data-valor="frete"]')
            ).to_have_text("R$ 0,00")

            expect(
                page.locator('dd[data-valor="total"]')
            ).to_have_text("R$ 200,00")

            page.locator('a[href="/checkout"]').click()

            expect(page).to_have_url(
                "https://verzel-store.qa-test-verzel-store.workers.dev/checkout"
            )

        finally:
            browser.close()
