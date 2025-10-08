import re
import json

# Define the path to your extracted text file
input_file = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/extracted_text.txt"  # Replace with your actual file path
output_file = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/parsed_receipts.json"  # Output file to save parsed data

# Function to parse each receipt
def parse_receipt(receipt_text):
    parsed_data = {}

    # Detect store name
    store_name_match = re.search(r"([A-Za-z\s]+(?:Restaurant|Store|Shop))", receipt_text)
    parsed_data['store_name'] = store_name_match.group(1) if store_name_match else "Unknown Store"

    # Detect address (usually near the top, after store name)
    address_match = re.search(r"(\d{1,5}\s[\w\s]+(?:\s(?:ST|STE|AVENUE|BLVD)[\d\s,]+))", receipt_text)
    parsed_data['address'] = address_match.group(1) if address_match else "Unknown Address"

    # Detect order number
    order_match = re.search(r"(?:Order|Check|Ticket)\s*[:\s]*(\d+)", receipt_text)
    parsed_data['order_number'] = order_match.group(1) if order_match else "Unknown Order"

    # Detect cashier's name
    cashier_match = re.search(r"Cashier\s*[:\s]*([A-Za-z\s]+)", receipt_text)
    parsed_data['cashier'] = cashier_match.group(1) if cashier_match else "Unknown Cashier"

    # Detect date and time
    date_time_match = re.search(r"(\d{1,2}-[A-Za-z]+-\d{4}\s\d{1,2}:\d{2}(:\d{2})?[APM]{1,2})", receipt_text)
    parsed_data['date_time'] = date_time_match.group(1) if date_time_match else "Unknown Date & Time"

    # Detect items: Example format '1 Curry Chicken $10.00'
    items = []
    for match in re.finditer(r"(\d+)\s([A-Za-z\s]+)\s\$(\d+\.\d{2})", receipt_text):
        item_name = match.group(2).strip()
        item_price = float(match.group(3))
        items.append({'item_name': item_name, 'price': item_price})
    parsed_data['items'] = items

    # Detect total and tax amounts
    total_match = re.search(r"Total\s*\$(\d+\.\d{2})", receipt_text)
    parsed_data['total'] = float(total_match.group(1)) if total_match else 0.0
    
    tax_match = re.search(r"Tax\s*\$(\d+\.\d{2})", receipt_text)
    parsed_data['tax'] = float(tax_match.group(1)) if tax_match else 0.0

    return parsed_data

# Read the text file containing the extracted receipt data
with open(input_file, 'r') as file:
    extracted_text = file.read()

# Split the file into separate receipts (assuming each receipt is separated by '---')
receipts = extracted_text.split("\n---")

# Parse each receipt and store the parsed data
parsed_receipts = []
for receipt in receipts:
    if receipt.strip():  # Avoid processing empty receipts
        parsed_receipts.append(parse_receipt(receipt.strip()))

# Save the parsed data to a JSON file
with open(output_file, 'w') as output_file:
    json.dump(parsed_receipts, output_file, indent=4)

print(f"Parsed data saved to {output_file}")
