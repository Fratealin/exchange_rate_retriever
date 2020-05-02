import csv
from os import path


def create_csv_file(filename):
    if not path.exists(filename):
        csv_header = ['Date', 'Exchange rate']
        with open(filename, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(csv_header)
            csv_file.close()


def read_csv(filename):
    with open(filename, mode='r') as csv_file:
        exchange_rates = [row["Exchange rate"] for row in csv.DictReader(csv_file)]
        #convert exchange rates to float
        [float(i) for i in exchange_rates]
        csv_file.close()
        return exchange_rates


def write_csv(new_csv_data):
    with open(new_csv_data[0], mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(new_csv_data[1:])
        csv_file.close()



