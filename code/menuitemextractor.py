if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from menuitem import MenuItem



def clean_price(price: str) -> float:
    """Cleans a string price like '$9.99' or '$1,299.50' and returns a float."""
    return float(price.replace('$', '').replace(',', '').strip())


def clean_scraped_text(scraped_text: str) -> list[str]:
    """Cleans the raw scraped menu text and filters out unwanted items."""
    lines = scraped_text.split("\n")
    cleaned = []
    skip_terms = {"NEW!", "NEW", "S", "V", "GS", "P"}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.upper() in skip_terms:
            continue
        cleaned.append(line)

    return cleaned


def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    """Converts the category and scraped text into a MenuItem dataclass."""
    cleaned = clean_scraped_text(scraped_text)
    
    name = cleaned[0]
    price = clean_price(cleaned[1])
    description = cleaned[2] if len(cleaned) > 2 else "No description available"

    return MenuItem(category=title, name=name, price=price, description=description)


if __name__ == '__main__':
    pass  
