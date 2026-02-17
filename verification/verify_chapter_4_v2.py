from playwright.sync_api import sync_playwright

def verify(page):
    print("Navigating to home...")
    page.goto("http://localhost:5173/")

    # Check if link exists
    link = page.locator("a[href*='capitulo-4']")
    if link.count() > 0:
        print("Link found!")
        link.first.click()
        print("Clicked link, waiting for navigation...")
        page.wait_for_url("**/capitulos/capitulo-4")
        print("Navigation successful.")
    else:
        print("Link NOT found on home page. Trying direct navigation.")
        page.goto("http://localhost:5173/capitulos/capitulo-4")

    # Verify content
    content = page.content()
    if "Sombras e Sinapses" in content:
        print("Title found.")
    else:
        print("Title NOT found.")

    if "Sobrecarga Sináptica" in content:
        print("Content found.")
    else:
        print("Content NOT found.")

    page.screenshot(path="verification/chapter_4_v2.png", full_page=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    try:
        verify(page)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        browser.close()
