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
