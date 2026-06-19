import csv

def create_reader(file_obj):
    return csv.DictReader(file_obj)
