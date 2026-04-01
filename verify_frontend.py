from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            base_url = "http://localhost:4173"
            targets = [
                ("/", "verification_home_updated.png", "Home"),
                ("/public/capitulos/capitulo-44", "verification_chapter_44.png", "Capítulo 44"),
                ("/personagens", "verification_personagens_updated.png", "Personagens")
            ]
            for path, img, label in targets:
                response = page.goto(f"{base_url}{path}")
                if response and response.status == 200:
                    page.screenshot(path=img)
                    print(f"Screenshot de {label} salvo.")
                else:
                    print(f"Falha ao carregar {label}: {response.status if response else 'N/A'}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_frontend()