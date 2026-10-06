"""
Receipt Parser - Practice 5
This script reads raw.txt (a real pharmacy receipt) and uses regex
to pull out prices, product names, the total, date/time and payment method.
"""

import re
import json


def load_receipt_text(file_path):
    """Read the whole receipt file as one text string."""
    with open(file_path, "r", encoding="utf-8") as receipt_file:
        return receipt_file.read()


def money_to_number(money_text):
    """
    Convert a price written like '1 200,00' into a normal float 1200.0
    In this receipt, spaces separate thousands and comma is the decimal point.
    """
    cleaned_text = money_text.replace(" ", "").replace(",", ".")
    return float(cleaned_text)


def extract_products(receipt_text):
    """
    Find every product line in the receipt.
    Each product in raw.txt always looks like this:

        5.
        Шприц 5 мл, 3-х комп.
        1,000 x 310,00
        310,00
        Стоимость
        310,00

    So I go line by line and look for the pattern: a line number,
    then the product name, then quantity x price, then the totals.
    """
    lines = receipt_text.splitlines()

    item_number_pattern = re.compile(r"^(\d+)\.$")
    quantity_price_pattern = re.compile(r"^([\d,]+)\s*x\s*([\d\s,]+)$")

    products = []
    line_index = 0

    while line_index < len(lines):
        current_line = lines[line_index].strip()

        # Here I check if this line is just a number with a dot, like "5."
        number_match = item_number_pattern.match(current_line)

        if number_match and line_index + 5 < len(lines):
            product_name = lines[line_index + 1].strip()
            quantity_price_line = lines[line_index + 2].strip()
            qty_price_match = quantity_price_pattern.match(quantity_price_line)

            if qty_price_match:
                quantity_text = qty_price_match.group(1)
                unit_price_text = qty_price_match.group(2)
                line_total_text = lines[line_index + 3].strip()

                products.append({
                    "position": int(number_match.group(1)),
                    "name": product_name,
                    "quantity": money_to_number(quantity_text),
                    "unit_price": money_to_number(unit_price_text),
                    "total_price": money_to_number(line_total_text),
                })

                line_index += 6  # Skip to the next item block
                continue

        line_index += 1

    return products


def extract_total_amount(receipt_text):
    """Find the total sum after the word 'ИТОГО:'"""
    total_pattern = re.search(r"ИТОГО:\s*\n?\s*([\d\s,]+)", receipt_text)
    if total_pattern:
        return money_to_number(total_pattern.group(1))
    return None


def extract_payment_method(receipt_text):
    """
    Find how the customer paid.
    The receipt shows something like 'Банковская карта:' or 'Наличные:'
    right before the total amount.
    """
    payment_pattern = re.search(
        r"(Банковская карта|Наличные|Наличными)\s*:\s*\n?\s*([\d\s,]+)",
        receipt_text,
    )
    if payment_pattern:
        method_name = payment_pattern.group(1)
        amount_paid = money_to_number(payment_pattern.group(2))
        return {"method": method_name, "amount": amount_paid}
    return None


def extract_date_and_time(receipt_text):
    """Find the date and time, written like '18.04.2019 11:13:58'"""
    date_time_pattern = re.search(
        r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})",
        receipt_text,
    )
    if date_time_pattern:
        return {"date": date_time_pattern.group(1), "time": date_time_pattern.group(2)}
    return None


def extract_receipt_number(receipt_text):
    """Find the receipt number, written like 'Чек №2331180266'"""
    receipt_number_pattern = re.search(r"Чек\s*№(\d+)", receipt_text)
    if receipt_number_pattern:
        return receipt_number_pattern.group(1)
    return None


def build_parsed_receipt(receipt_text):
    """Put everything together into one dictionary."""
    products = extract_products(receipt_text)

    return {
        "receipt_number": extract_receipt_number(receipt_text),
        "date_time": extract_date_and_time(receipt_text),
        "products": products,
        "number_of_products": len(products),
        "total_amount": extract_total_amount(receipt_text),
        "payment": extract_payment_method(receipt_text),
    }


def print_receipt_report(parsed_receipt):
    """Print the parsed data in a readable format."""
    print("=" * 50)
    print("RECEIPT REPORT")
    print("=" * 50)
    print("Receipt number:", parsed_receipt["receipt_number"])

    if parsed_receipt["date_time"]:
        print("Date:", parsed_receipt["date_time"]["date"])
        print("Time:", parsed_receipt["date_time"]["time"])

    print("-" * 50)
    print("PRODUCTS:")
    for product in parsed_receipt["products"]:
        print(
            f"{product['position']:>2}. {product['name']} | "
            f"{product['quantity']} x {product['unit_price']} = {product['total_price']}"
        )

    print("-" * 50)
    print("Total number of products:", parsed_receipt["number_of_products"])
    print("Total amount:", parsed_receipt["total_amount"])

    if parsed_receipt["payment"]:
        print("Payment method:", parsed_receipt["payment"]["method"])
        print("Amount paid:", parsed_receipt["payment"]["amount"])
    print("=" * 50)


if __name__ == "__main__":
    receipt_text = load_receipt_text("raw.txt")
    parsed_receipt = build_parsed_receipt(receipt_text)

    # Show a readable report in the terminal
    print_receipt_report(parsed_receipt)

    # Also save a structured JSON file, as the task asks
    with open("parsed_receipt.json", "w", encoding="utf-8") as json_file:
        json.dump(parsed_receipt, json_file, ensure_ascii=False, indent=4)

    print("\nSaved structured data to parsed_receipt.json")
