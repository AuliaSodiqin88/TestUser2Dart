import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sendbird-uikit-react.netlify.app/group_channel?appId=37C8DB25-8B44-435F-A528-5BA9B9965FD0&userId=Aulia%20Sendbird&nickname=Aulia")
    page.locator(".sendbird-iconbutton__inner > .sendbird-icon").first.click()
    time.sleep(10)
    page.get_by_role("button", name="Group").click()
    page.get_by_text("sendbird", exact=True).click()
    page.locator("div").filter(has_text=re.compile(r"^sendbird$")).locator("span").nth(1).click()
    page.get_by_role("button", name="Create").click()
    #page.get_by_role("link", name="User 2 Photo").click()
    page.locator("Text Input").click()
    expect(page.get_by_test_id("sendbird-message-list-container")).to_contain_text("June 17, 2024Aulia and User joined.9:59 AMtesting automate10:00 AM")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
