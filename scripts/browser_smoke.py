"""Isolated browser acceptance smoke test."""
import os, subprocess, sys, tempfile, time
from urllib.request import urlopen
from playwright.sync_api import sync_playwright, expect

BASE = "http://127.0.0.1:8766"
with tempfile.TemporaryDirectory() as directory:
    env = dict(os.environ, N25X_DB=directory + "/test.db")
    env.pop("LLM_API_KEY", None)
    env.pop("LLM_MODEL", None)
    server = subprocess.Popen([sys.executable, "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8766"], env=env)
    try:
        for _ in range(60):
            try:
                with urlopen(BASE + "/api/health", timeout=1):
                    break
            except OSError:
                time.sleep(.2)
        else:
            raise RuntimeError("API failed to start")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width":390,"height":844})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(BASE)
            expect(page.locator("#health")).to_contain_text("ONLINE")
            page.locator("#language").select_option("en")
            expect(page.locator("[data-i=library]")).to_have_text("Document library")
            page.locator("#theme").select_option("ocean")
            page.reload()
            expect(page.locator("#language")).to_have_value("en")
            expect(page.locator("#theme")).to_have_value("ocean")
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("What are the support hours?")
            page.locator("#ask button").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            expect(page.locator("#answer a")).to_have_attribute("href", "#source-S1")
            page.locator("#answer a").click()
            expect(page).to_have_url(BASE + "/#source-S1")
            page.locator("#language").select_option("de")
            expect(page.locator("[data-i=library]")).to_have_text("Dokumentenbibliothek")
            expect(page.locator("#answer")).to_contain_text("Support hours")
            page.locator("#question").fill("Quantenmechanik")
            page.locator("#ask button").click()
            expect(page.locator("#answer")).to_have_text("Keine passenden Textstellen gefunden.")
            page.locator("#docs button").click()
            expect(page.locator("#docs")).to_contain_text("Noch keine Dokumente.")
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
            page.set_viewport_size({"width":1280,"height":800})
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("Was ist die Supportzeit?")
            page.locator("#ask button").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            page.locator("#theme").select_option("light")
            page.locator("#language").select_option("ru")
            expect(page.locator("[data-i=library]")).to_have_text("Библиотека документов")
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("Какое время поддержки?")
            page.locator("#depth").select_option("1")
            page.locator("#ask button").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            with page.expect_download() as download:
                page.locator("#export").click()
            assert download.value.suggested_filename == "n25x-research.txt"
            page.locator("#none").click()
            page.locator("#ask button").click()
            expect(page.locator("#answer")).to_have_text("Подходящих фрагментов не найдено.")
            page.reload()
            expect(page.locator("#language")).to_have_value("ru")
            assert not errors, errors
            browser.close()
            print("Browser smoke passed")
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()
            server.wait()
