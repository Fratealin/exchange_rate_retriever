
def get_trip_destination(currencies):
    print("\n".join(currencies))
    destination_currency = input("What currency do you need for your holiday or business trip? ")
    match = False
    while not match:
        for currency in currencies:
            if currency.find(destination_currency) == -1:
                continue
            else:
                match = True
        if match:
            break
        destination_currency = input("Please type correct currency: ")
    return destination_currency
