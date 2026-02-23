from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    print("Navigating to Chapter 11...")
    page.goto("http://localhost:3000/capitulos/capitulo-11")

    # Wait for content to load
    page.wait_for_selector("h1")

    # Verify Title
    title = page.locator("h1").inner_text()
    print(f"Page Title: {title}")
    assert "Convergência Sombria" in title

    # Verify Content
    content = page.content()
    assert "O silêncio que se seguiu ao massacre não era paz." in content
    assert "Jaxon ainda respirava" in content

    print("Content verification passed.")

    # Take screenshot
    page.screenshot(path="verification_chapter_11.png")
    print("Screenshot saved to verification_chapter_11.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
