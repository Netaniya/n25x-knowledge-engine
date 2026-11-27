"""Isolated browser acceptance smoke test."""
import os, subprocess, sys, tempfile, time
from urllib.request import urlopen
from playwright.sync_api import sync_playwright, expect

BASE = "http://127.0.0.1:8766"
with tempfile.TemporaryDirectory() as directory:
    env = dict(os.environ, N25X_DB=directory + "/test.db")
    env.pop("LLM_API_KEY", None)
    env.pop("LLM_MODEL", None)
    for key in ("LOCAL_EMBED_MODEL", "CLOUD_EMBED_MODEL", "CLOUD_EMBED_API_KEY"):
        env.pop(key, None)
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
            expect(page).to_have_title("N25X NOESIS")
            expect(page.locator("header img[alt=N25X]")).to_be_visible()
            assert page.locator("header img[alt=N25X]").evaluate("(img) => img.complete && img.naturalWidth > 0")
            expect(page.locator("#generate")).to_be_disabled()
            expect(page.locator("#search-mode option[value=local]")).to_have_attribute("disabled", "")
            expect(page.locator("#search-mode option[value=cloud]")).to_have_attribute("disabled", "")
            expect(page.locator("#library-panel")).to_be_hidden()
            expect(page.locator("#library-toggle")).to_have_attribute("aria-expanded", "false")
            expect(page.locator("#question")).to_be_visible()
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
            assert page.locator("#workspace-panel").bounding_box()["width"] >= 0.94 * 390
            page.locator("#library-toggle").click()
            expect(page.locator("#library-panel")).to_be_visible()
            page.locator("#language").select_option("en")
            expect(page.locator("[data-i=library]")).to_have_text("Document library")
            page.locator("#theme").select_option("ocean")
            page.reload()
            expect(page.locator("#language")).to_have_value("en")
            expect(page.locator("#theme")).to_have_value("ocean")
            page.locator("#library-toggle").click()
            expect(page.locator("#library-panel")).to_be_visible()
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("What are the support hours?")
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            expect(page.locator("#answer a")).to_have_attribute("href", "#source-S1")
            page.locator("#answer a").click()
            expect(page).to_have_url(BASE + "/#source-S1")
            page.locator("#language").select_option("de")
            expect(page.locator("[data-i=library]")).to_have_text("Dokumentenbibliothek")
            expect(page.locator("#answer")).to_contain_text("Support hours")
            page.locator("#question").fill("Quantenmechanik")
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_have_text("Keine passenden Textstellen gefunden.")
            page.locator("#docs button").click()
            expect(page.locator("#docs")).to_contain_text("Noch keine Dokumente.")
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
            page.set_viewport_size({"width":1280,"height":800})
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("Was ist die Supportzeit?")
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            page.locator("#theme").select_option("light")
            page.locator("#language").select_option("ru")
            expect(page.locator("[data-i=library]")).to_have_text("Библиотека документов")
            page.locator("#demo").click()
            expect(page.locator("#question")).to_have_value("Какое время поддержки?")
            page.locator("#depth").select_option("1")
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            with page.expect_download() as download:
                page.locator("#export").click()
            assert download.value.suggested_filename == "n25x-research.txt"
            page.locator("#none").click()
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_have_text("Подходящих фрагментов не найдено.")
            page.reload()
            expect(page.locator("#language")).to_have_value("ru")
            page.locator("#language").select_option("en")
            page.locator("#file").set_input_files({"name":"owner-qa-sample.txt","mimeType":"text/plain","buffer":b"Test record. The verification code is Kestrel-481."})
            page.locator("#upload button[data-i=upload]").click()
            expect(page.locator("#docs")).to_contain_text("owner-qa-sample.txt")
            page.locator("#none").click()
            selected = page.locator(".doc").filter(has_text="owner-qa-sample.txt").locator("input")
            selected.check()
            expect(page.locator("#selection")).to_contain_text("1 /")
            page.locator("#question").fill("verification code")
            page.locator("#ask button[data-i=search]").click()
            expect(page.locator("#answer")).to_contain_text("Kestrel-481")
            expect(page.locator("#sources .source")).to_have_count(1)
            page.locator("#all").click()
            assert page.locator(".doc input:checked").count() == page.locator(".doc input").count()
            page.locator("#library-toggle").click()
            expect(page.locator("#library-panel")).to_be_hidden()
            page.locator("#language").select_option("ru")
            expect(page.locator("#library-toggle")).to_have_text("Показать библиотеку")
            page.locator("#library-toggle").click()
            expect(page.locator("#library-panel")).to_be_visible()
            assert page.locator("footer a").get_attribute("href") == "/docs"
            with page.expect_navigation():
                page.locator("footer a").click()
            expect(page).to_have_url(BASE + "/docs")
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
