import sys
from barcode_displayer import barcode_displayer

while True:
    input_val = input()
    if input_val:
        barcode_displayer(str(input_val))
        input_val = None
