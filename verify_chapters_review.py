from playwright.sync_api import sync_playwright

def verify_chapters():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Navigate to Chapter 50
            page.goto("http://localhost:4173/public/capitulos/capitulo-50.html")

            # Wait for content to load
            page.wait_for_selector("h1")

            # Take screenshot
            page.screenshot(path="verification_chapter_50_review.png", full_page=True)
            print("Screenshot taken: verification_chapter_50_review.png")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_chapters()
