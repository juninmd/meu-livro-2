from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verifica Página Inicial
        page.goto("http://localhost:4173/")
        page.screenshot(path="verification_home_updated.png")
        print("Screenshot da Home atualizado salvo.")

        # Verifica Capítulo 44
        page.goto("http://localhost:4173/public/capitulos/capitulo-44")
        page.screenshot(path="verification_chapter_44.png")
        print("Screenshot do Capítulo 44 salvo.")

        # Verifica Personagens
        page.goto("http://localhost:4173/personagens")
        page.screenshot(path="verification_personagens_updated.png")
        print("Screenshot de Personagens atualizado salvo.")

        browser.close()

if __name__ == "__main__":
    verify_frontend()