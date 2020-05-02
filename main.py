import get_exchange_rate_data
import datetime
import file_writer
import email_manager
import get_trip_destination
import time


# get email update every 24 hrs
def get_daily_exchange_rate():
    currencies = get_exchange_rate_data.get_currencies_list()
    destination_currency = get_trip_destination.get_trip_destination(currencies)

    for day in range(5):
        today = datetime.datetime.now()
        if today.strftime("%A") in ["Saturday", "Sunday"]:
            print("As there is no exchange rate data on weekends, we will provide it on Monday.")
            oneDay = 60*60*24
            time.sleep(oneDay)
            continue

        todaysRate = get_exchange_rate_data.get_exchange_rate_data(destination_currency)
        file_name = todaysRate[0] + "_exchange_rates.txt"
        file_writer.create_csv_file(file_name)

        date = today.strftime("%A %B %d %Y, %H:%M")
        new_csv_data = [file_name, date, todaysRate[1]]
        file_writer.write_csv(new_csv_data)

        previousRates = file_writer.read_csv(file_name)
        email_manager.create_email(previousRates, date, todaysRate)

        oneDay = 60*60*24
        time.sleep(oneDay)


get_daily_exchange_rate()
