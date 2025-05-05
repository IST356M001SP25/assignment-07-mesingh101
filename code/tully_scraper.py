import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    page.wait_for_timeout(3000)

    all_items = []

    # Locate all menu section titles
    titles = page.locator("h3.foodmenu__menu-section-title")
    count = titles.count()

    for i in range(count):
        title_element = titles.nth(i)
        title_text = title_element.inner_text().strip()
        print(f"\nMENU SECTION: {title_text}")

        # Go two siblings forward to get the corresponding row of items
        row_element = title_element.evaluate_handle("el => el.nextElementSibling?.nextElementSibling")

        # Playwright handle must be converted to an element handle for querying
        row_element = row_element.as_element()

        if row_element:
            item_elements = row_element.query_selector_all("div.foodmenu__menu-item")

            for item in item_elements:
                item_text = item.inner_text().strip()
                if not item_text:
                    continue
                try:
                    menu_obj = extract_menu_item(title_text, item_text)
                    print(f"  MENU ITEM: {menu_obj.name}")
                    all_items.append(menu_obj.to_dict())
                except Exception as e:
                    print(f"  Skipping item under '{title_text}' due to error: {e}")

    # Ensure cache directory exists
    os.makedirs("cache", exist_ok=True)

    # Export data to CSV
    df = pd.DataFrame(all_items)
    df.to_csv("cache/tullys_menu.csv", index=False)

    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        tullyscraper(playwright)
