from playwright.sync_api import sync_playwright

def verify_chapter(page):
    # Navigate to the home page first to check nav link
    page.goto("http://localhost:5173/")

    # Click on the new chapter link in the navbar or sidebar
    # Depending on screen size, sidebar might be hidden, so let's try direct navigation first
    # but the goal is to verify the link exists.

    # Let's try to find the link "Capítulo 4"
    # Note: Text might be "Capítulo 4" in Nav or "Capítulo 4: Sombras e Sinapses" in Sidebar

    page.click("text=Capítulo 4")

    # Wait for navigation
    page.wait_for_url("**/capitulos/capitulo-4")

    # Check for specific content from the chapter
    assert "Sombras e Sinapses" in page.content()
    assert "Sobrecarga Sináptica" in page.content()

    # Take a screenshot
    page.screenshot(path="verification/chapter_4_proof.png", full_page=True)
    print("Screenshot taken successfully")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    try:
        verify_chapter(page)
    except Exception as e:
        print(f"Error: {e}")
        # Take a screenshot of the error state
        page.screenshot(path="verification/error_state.png")
    finally:
        browser.close()
