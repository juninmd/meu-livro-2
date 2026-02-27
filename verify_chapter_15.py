from playwright.sync_api import sync_playwright
import time

def verify_chapter(page):
    # Navigate to the home page
    print("Navigating to home page...")
    page.goto("http://localhost:3000/")
    time.sleep(2)  # Wait for hydration

    # Take screenshot of home page
    page.screenshot(path="verification_home.png")
    print("Home page screenshot taken.")

    # Navigate to Chapter 15
    print("Navigating to Chapter 15...")
    page.goto("http://localhost:3000/capitulos/capitulo-15")
    time.sleep(2)  # Wait for content load

    # Take screenshot of Chapter 15
    page.screenshot(path="verification_chapter_15.png")
    print("Chapter 15 screenshot taken.")

    # Verify content
    content = page.content()
    if "Permuta Sináptica" in content:
        print("SUCCESS: Chapter title found.")
    else:
        print("FAILURE: Chapter title not found.")

    if "Dr. Vex" in content:
        print("SUCCESS: Character Dr. Vex found.")
    else:
        print("FAILURE: Character Dr. Vex not found.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_chapter(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
