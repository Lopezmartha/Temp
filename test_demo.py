from playwright.sync_api import Page

def test_demo(page:Page):
    page.goto("https://google.com")