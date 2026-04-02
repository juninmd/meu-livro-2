from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Navigate to the Home page and ensure the new chapter is visible
    page.goto("http://localhost:4173/")
    page.wait_for_timeout(1000)

    # Scroll down slightly to make sure the chapter list is in view
    page.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/verification_home_updated.png")

    # Navigate to Chapter 45
    page.goto("http://localhost:4173/public/capitulos/capitulo-45.html")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/verification_chapter_45.png")

    # Navigate to Personagens page
    page.goto("http://localhost:4173/personagens.html")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/verification_personagens_cap45.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    import os
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()