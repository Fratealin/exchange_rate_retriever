import requests
import bs4


def get_currencies_list():
    countries_soup = get_html_elements("td > a")
    currencies = []
    for line in countries_soup:
        Text = line.getText()
        currencies.append(Text)
    return currencies


def get_html_elements(row_selector):
    #TODO
    path = "https://www.bankofengland.co.uk/boeapps/database/Rates.asp?Travel=NIxAZx&into=GBP"
    path = "https://www.bankofengland.co.uk/boeapps/database/Rates.asp?TD=29&TM=Apr&TY=2020&into=GBP&rateview=D"
    soup = get_html_object(path)
    elements = soup.select(row_selector)
    return elements


def get_html_object(path):
    #open webpage
    result = requests.get(path)
    try:
        result.raise_for_status()
    except Exception as exc:
        print("There was a problem: %s" % (exc))
    # return soup, aka html object
    return bs4.BeautifulSoup(result.text, 'html.parser')


def get_exchange_rate_data(destination_currency):
    rows = get_html_elements("tr")
    for row in rows[1:]:
        text = row.getText()

        if text.find(destination_currency) == -1:
            continue
        else:
            split_text = text.strip().split("\n")
            country = split_text[0]
            currency = split_text[1].strip()
            return [country, currency]
