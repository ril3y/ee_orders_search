import os
import csv
import argparse
import re
import pyperclip
from termcolor import colored

def parse_lcsc_orders_file(file_path):
    orders = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            orders.append({
                'Source': 'LCSC',
                'LCSC Part Number': row[0],
                'Manufacturer Part Number': row[1],
                'Manufacturer': row[2],
                'Customer NO.': row[3],
                'Package': row[4],
                'Description': row[5],
                'RoHS': row[6],
                'Order Qty.': row[7],
                'Min/Mult Order Qty.': row[8],
                'Unit Price($)': row[9],
                'Order Price($)': row[10]
            })
    return orders

def parse_digikey_orders_file(file_path):
    orders = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) >= 8:  # Ensure row has enough columns
                orders.append({
                    'Source': 'DigiKey',
                    'DigiKey Part Number': row[1],
                    'Manufacturer Part Number': row[2],
                    'Description': row[3],
                    'Customer Reference': row[4],
                    'Quantity': row[5],
                    'Backorder': row[6],
                    'Unit Price($)': row[7],
                    'Extended Price($)': row[8]
                })
    return orders

def search_orders(orders, query, search_type='lcsc'):
    results = []
    for order in orders:
        # Search logic based on search type
        if search_type == 'lcsc':
            if (order['Source'] == 'LCSC' and 
                (order['LCSC Part Number'] == query or 
                 order['LCSC Part Number'].startswith(query.rstrip('*')))):
                results.append(order)
        elif search_type == 'manufacturer':
            # Case-insensitive partial match for manufacturer part number
            if (query.lower() in order['Manufacturer Part Number'].lower() or 
                order['Manufacturer Part Number'].lower().startswith(query.lower().rstrip('*'))):
                results.append(order)
        elif search_type == 'digikey':
            # Search DigiKey Part Number
            if (order['Source'] == 'DigiKey' and 
                (order['DigiKey Part Number'] == query or 
                 order['DigiKey Part Number'].startswith(query.rstrip('*')))):
                results.append(order)
    return results

def validate_lcsc_part_number(part_number):
    # Regex pattern for LCSC part numbers
    # Starts with C followed by 4-7 digits
    pattern = r'^C\d{4,7}'
    return re.match(pattern, part_number) is not None

def print_results(results):
    if results:
        print(colored('Search Results:', 'green'))
        for i, result in enumerate(results, 1):
            print(colored(f'Result {i}:', 'yellow'))
            print(colored(f'  Source:', 'cyan'), result['Source'])
            
            # Print different keys based on source
            if result['Source'] == 'LCSC':
                keys_to_print = [
                    'LCSC Part Number', 'Manufacturer Part Number', 
                    'Manufacturer', 'Customer NO.', 'Package', 
                    'Description', 'RoHS', 'Order Qty.', 
                    'Min/Mult Order Qty.', 'Unit Price($)', 'Order Price($)'
                ]
            else:  # DigiKey
                keys_to_print = [
                    'DigiKey Part Number', 'Manufacturer Part Number', 
                    'Description', 'Customer Reference', 
                    'Quantity', 'Backorder', 
                    'Unit Price($)', 'Extended Price($)'
                ]
            
            for key in keys_to_print:
                if key in result:
                    print(f'  {colored(key + ":", "cyan")} {result[key]}')
            
            print()  # blank line between results
    else:
        print(colored('No results found.', 'red'))

def main():
    parser = argparse.ArgumentParser(description='Search LCSC and DigiKey orders')
    parser.add_argument('--orders', default='.', help='Path to orders directory (default: current directory)')
    parser.add_argument('--lcsc_pn', action='store_true', help='Search by LCSC part number')
    parser.add_argument('--pn', action='store_true', help='Search by Manufacturer part number')
    parser.add_argument('--digi_pn', action='store_true', help='Search by DigiKey part number')
    parser.add_argument('query', nargs='?', help='Search query')

    args = parser.parse_args()

    # Find all CSV files in the specified or default directory
    orders_files = [
        os.path.join(args.orders, f) 
        for f in os.listdir(args.orders) 
        if f.endswith('.csv')
    ]

    # Collect orders from all files
    all_orders = []
    for file_path in orders_files:
        # Try parsing as LCSC orders first
        try:
            all_orders.extend(parse_lcsc_orders_file(file_path))
        except Exception:
            # If LCSC parsing fails, try DigiKey parsing
            try:
                all_orders.extend(parse_digikey_orders_file(file_path))
            except Exception:
                print(f"Could not parse file: {file_path}")

    # Determine search query and type
    query = args.query
    search_type = 'lcsc'  # default search type

    if args.pn:
        search_type = 'manufacturer'
    elif args.digi_pn:
        search_type = 'digikey'

    if not query:
        # If no query provided, check clipboard
        clipboard_content = pyperclip.paste().strip()
        if validate_lcsc_part_number(clipboard_content):
            query = clipboard_content
        else:
            print(colored('No valid LCSC part number found in clipboard.', 'red'))
            return

    # Perform search
    results = search_orders(all_orders, query, search_type)

    # Print results
    print_results(results)

if __name__ == '__main__':
    main()