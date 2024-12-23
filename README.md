# EE Orders Search 

A Python script to search through LCSC and DigiKey order files. 

## Installation  

```bash 
pip install -r requirements.txt  
``` 

## Usage  

Search LCSC Part Number:  
```bash  
python ee_search.py --orders ./orders C130253  
``` 

Search Manufacturer Part Number:  
```bash  
python ee_search.py --orders ./orders --pn MCP  
``` 

Search DigiKey Part Number:  
```bash  
python ee_search.py --orders ./orders --digi_pn MCP2515-I/SO-ND  
``` 

## Features  
- Search across multiple order sources  
- Supports LCSC and DigiKey order formats  
- Clipboard integration  
- Flexible part number searching  

## Example Output
```bash  
python .\ee_search.py --pn MCP --order .\orders\
Search Results:

Result 1:
  Source: DigiKey
  DigiKey Part Number: MCP2515-I/SO-ND
  Manufacturer Part Number: MCP2515-I/SO
  Description: IC CAN CONTROLLER W/SPI 18SOIC
  Customer Reference: GCART
  Quantity: 3
  Backorder: 0
  Unit Price($): $2.44000
  Extended Price($): $7.32

Result 2:
  Source: LCSC
  LCSC Part Number: C150772
  Manufacturer Part Number: MCP73831-2ACI/MC
  Manufacturer: Microchip Tech
  Customer NO.: GPS_MODULE
  Package: TDFN-8-EP(2x3)
  Description: TDFN-8-EP(2x3) Battery Management ROHS
  RoHS: YES
  Order Qty.: 5
  Min/Mult Order Qty.: 1\1
  Unit Price($): 1.4207
  Order Price($): 7.10

Result 3:
  Source: LCSC
  LCSC Part Number: C511310
  Manufacturer Part Number: MCP73871T-2CCI/ML
  Manufacturer: Microchip Tech
  Customer NO.: 10
  Package: QFN-20-EP(4x4)
  Description: 6V Lithium-ion/Polymer 1 1A QFN-20-EP(4x4) Battery Management ROHS
  RoHS: YES
  Order Qty.: 10
  Min/Mult Order Qty.: 1\1
  Unit Price($): 1.2091
  Order Price($): 12.09
``` 