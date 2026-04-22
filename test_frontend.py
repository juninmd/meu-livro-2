from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:4173/public/capitulos/capitulo-65.html')

    title = page.title()
    assert "A Engrenagem Analógica" in title, f"Expected title to contain 'A Engrenagem Analógica', but got '{title}'"

    page.goto('http://localhost:4173/')
    assert "Capítulo 65" in page.content(), "Expected to find Chapter 65 link on home page"

    browser.close()
    print("Frontend tests passed!")
