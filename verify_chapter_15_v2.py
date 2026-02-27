from playwright.sync_api import sync_playwright
import time

def verify_chapter(page):
    # Navigate to the home page
    print("Navigating to home page...")
    page.goto("http://localhost:3000/")
    time.sleep(2)  # Wait for hydration

    # Check if link exists in sidebar
    try:
        # The sidebar links are usually in an aside or nav.
        # Let's look for the text "Capítulo 15: Permuta Sináptica"
        link = page.get_by_role("link", name="Capítulo 15: Permuta Sináptica")
        if link.count() > 0:
             print("SUCCESS: Chapter 15 link found in navigation/sidebar.")
             link.first.scroll_into_view_if_needed()
        else:
             print("FAILURE: Chapter 15 link NOT found in navigation/sidebar.")
    except Exception as e:
        print(f"Error checking sidebar: {e}")

    # Navigate to Chapter 15 directly
    print("Navigating to Chapter 15...")
    page.goto("http://localhost:3000/capitulos/capitulo-15")
    time.sleep(2)

    # Take screenshot of Chapter 15
    page.screenshot(path="verification_chapter_15_v2.png", full_page=True)
    print("Chapter 15 screenshot taken (full page).")

    # Verify content
    content = page.content()
    if "Permuta Sináptica" in content:
        print("SUCCESS: Chapter title found in content.")
    else:
        print("FAILURE: Chapter title NOT found in content.")

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
