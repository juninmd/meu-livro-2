from playwright.sync_api import sync_playwright, expect
import time

def verify_chapter_50():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to the local dev server
        page.goto("http://localhost:4173/public/capitulos/capitulo-50.html")

        # Wait a bit to let it render
        time.sleep(2)

        # Verify the title
        expect(page.locator("h1")).to_have_text("O Sangue Frio do Bunker")

        # Take a screenshot
        page.screenshot(path="verification_chapter_50.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_chapter_50()
