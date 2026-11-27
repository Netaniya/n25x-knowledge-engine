"""Test the actual portfolio-demo branch HTML in Chromium at both viewport sizes."""
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
root = Path("pages-checkout/index.html").resolve()
assert root.is_file()
with sync_playwright() as p:
    browser=p.chromium.launch()
    for width,height in [(390,844),(1280,800)]:
        page=browser.new_page(viewport={"width":width,"height":height},accept_downloads=True)
        errors=[]
        page.on("pageerror",lambda e:errors.append(str(e)))
        page.goto(root.as_uri())
        expect(page.locator("#language")).to_have_value("de")
        expect(page.locator("#copyright")).to_contain_text("Natalie Ragulina (Netaniya)")
        expect(page.locator("#health")).to_contain_text("ONLINE")
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        if width==390:
            expect(page.locator("#library-panel")).to_be_hidden()
            assert page.locator("#workspace-panel").bounding_box()["width"]>=width*.94
        else:
            expect(page.locator("#library-panel")).to_be_visible()
        for lang in ["de","ru","en"]:
            page.locator("#language").select_option(lang)
            page.locator("#quick-demo").click()
            expect(page.locator("#answer")).to_contain_text("17:00")
            expect(page.locator("#answer a").first).to_have_attribute("href","#source-S1")
        with page.expect_download() as event:
            page.locator("#export").click()
        download=event.value
        assert download.suggested_filename=="n25x-research.txt"
        contents=Path(download.path()).read_text(encoding="utf-8")
        assert "17:00" in contents and "[S1]" in contents and "N25X NOESIS" in contents
        if not page.locator("#library-panel").is_visible():
            page.locator("#library-toggle").click()
        page.locator("#file").set_input_files({"name":"custom-test.txt","mimeType":"text/plain","buffer":b"Project Quartz has budget 731 euros."})
        page.locator("#upload button[data-i=upload]").click()
        expect(page.locator("#docs")).to_contain_text("custom-test.txt")
        page.locator("#none").click()
        page.locator(".doc").filter(has_text="custom-test.txt").locator("input").check()
        page.locator("#question").fill("Quartz budget")
        page.locator("#ask button[data-i=search]").click()
        expect(page.locator("#answer")).to_contain_text("731")
        page.locator("#docs .doc").filter(has_text="custom-test.txt").locator("button").click()
        expect(page.locator("#docs")).not_to_contain_text("custom-test.txt")
        page.locator("#theme").select_option("light")
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        assert not errors,errors
        page.close()
    browser.close()
print("Portfolio Pages browser checks passed at 390 and 1280px; actual TXT download verified")
