import csv
from os import path
from datetime import date


######## functions ########

def make_new_list_file():
    file = open(f"List of Items_{date.today()}.csv", "w+")
    writer = csv.writer(file)
    writer.writerow("Beginning of this file".split(','))
    file.close()


def add_item_to_list_file(item):
    file = open(f"List of Items_{date.today()}.csv", "a")
    writer = csv.writer(file)
    writer.writerow(input_barcode.split(','))
    file.close()


######## Initialisation ########


######## Loop ########

while True:
    input_barcode = input()
    today_date = date.today()

    if not path.isfile((f"List of Items_{date.today()}.csv")):
        make_new_list_file()
    add_item_to_list_file(input_barcode)
