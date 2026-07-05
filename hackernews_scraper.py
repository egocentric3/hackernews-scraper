from playwright.sync_api import sync_playwright
import csv

def scrape():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://news.ycombinator.com")
            page.wait_for_selector("span.titleline")
            titles = page.query_selector_all("span.titleline")

            with open("hacker_news.csv", "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Sr No.","Title","URL"])
                for count, title in enumerate(titles, start=1):
                    link = title.query_selector("a")

                    if link:
                        writer.writerow([count, title.inner_text(), link.get_attribute("href")])
    except Exception as e:
        print(f"Connection error: {e}")
if __name__ == "__main__":
    scrape()
