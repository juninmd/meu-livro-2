from playwright.sync_api import sync_playwright

def verify(page):
    print("Navigating directly to chapter 4...")
    try:
        page.goto("http://localhost:5173/capitulos/capitulo-4", timeout=60000)
        print("Direct navigation successful.")

        content = page.content()
        if "Sombras e Sinapses" in content:
            print("Found title.")
        else:
            print("Title NOT found in direct load.")

        page.screenshot(path="verification/chapter_4_direct.png", full_page=True)
    except Exception as e:
        print(f"Direct navigation failed: {e}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    try:
        verify(page)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        browser.close()
