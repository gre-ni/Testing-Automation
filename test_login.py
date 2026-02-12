import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://partynotfound.datpp25.czechitas.online/prihlaseni")
    page.get_by_role("email", name="email").fill("unavenyrodic@email.cz")
    page.get_by_role("password", name="password").fill("Rodic123")
    page.get_by_role("submit", name="Přihlásit").click()
    
    
    