import asyncio
from playwright.async_api import async_playwright
import time

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        try:
            await page.goto("http://localhost:8001")

            # Wait for reveal.js to load
            await page.wait_for_selector(".reveal", timeout=10000)

            # Slide 1
            await page.screenshot(path="verification/slide1.png")
            print("Slide 1 captured")

            # Go to Slide 2
            await page.keyboard.press("ArrowRight")
            time.sleep(1.5)
            await page.screenshot(path="verification/slide2_initial.png")
            print("Slide 2 Initial captured")

            # Slide 2 Fragments (4 fragments)
            for i in range(4):
                await page.keyboard.press("ArrowRight")
                time.sleep(1.5)
                await page.screenshot(path=f"verification/slide2_frag_{i+1}.png")
                print(f"Slide 2 Fragment {i+1} captured")

            # Go to Slide 3 (Markdown)
            await page.keyboard.press("ArrowRight")
            time.sleep(1.5)
            await page.screenshot(path="verification/slide3_initial.png")
            print("Slide 3 Initial captured")

            # Slide 3 Fragments (3 bullets)
            for i in range(3):
                await page.keyboard.press("ArrowRight")
                time.sleep(1.5)
                await page.screenshot(path=f"verification/slide3_frag_{i+1}.png")
                print(f"Slide 3 Fragment {i+1} captured")

            # Go to Slide 4 (Code)
            await page.keyboard.press("ArrowRight")
            time.sleep(1.5)
            await page.screenshot(path="verification/slide4.png")
            print("Slide 4 captured")

        except Exception as e:
            print(f"Error: {e}")
            await page.screenshot(path="verification/error.png")

        await browser.close()

asyncio.run(run())
