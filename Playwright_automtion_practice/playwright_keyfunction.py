from playwright.sync_api import sync_playwright
browser= sync_playwright().start().chromium.launch(headless=True)
    page=browser.new_page()
    page.goto("https://www.google.com")
    page.screenshot(path="google.png")