from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:4173/public/capitulos/capitulo-64.html")
    page.wait_for_selector("h1")
    title = page.title()
    assert "O Ponto Cego" in title, f"Expected 'O Ponto Cego' in title, got: {title}"
    print("Capítulo 64 verified successfully.")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
