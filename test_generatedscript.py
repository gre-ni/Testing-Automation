import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    
    todo_item = page.get_by_role("textbox", name="What needs to be done?")
    todo_item.click()
    todo_item.fill("Jokes")
    todo_item.press("Enter")
    
    page.get_by_role("checkbox", name="Toggle Todo").check()
    page.get_by_role("button", name="Clear completed").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)