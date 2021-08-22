from bs4 import BeautifulSoup
import requests
import datetime
import operator
import json
import time

from multiprocessing import Pool


class Company:
    name = str
    ticker = str
    price = float
    one_year_gain = float
    pe_ratio = float
    potential_52_week_profit = float

    def __init__(self, name, ticker, price, one_year_gain, pe_ratio, potential_52_week_profit):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.one_year_gain = one_year_gain
        self.pe_ratio = pe_ratio
        self.potential_52_week_profit = potential_52_week_profit

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# get data of company
def walk_on_the_page(page_num):
    company_list = list()

    # get data from main page
    print(f"Processing page number {page_num}")
    company_name_dict = dict()
    html_text_page = requests.get(f'https://markets.businessinsider.com/index/components/s&p_500?p={page_num}', timeout=5).text

    content_from_page = BeautifulSoup(html_text_page, "html.parser")
    table_data = content_from_page.find('table', {'class': 'table table__layout--fixed'})

    # get link, year profit and name
    for data in table_data.findAll('tr')[1:]:
        name = data.findAll('td')[0].text
        year_profit = data.findAll('td')[7].text.split()[1].strip()
        clean_year_profit = float(year_profit.replace("%", ""))
        link = data.find('td', class_='table__td table__td--big').a.get('href')
        company_name_dict[name.strip()] = [link.strip(), clean_year_profit]

    # get data from company page
    for key in company_name_dict:

        i = company_name_dict[key]
        html_text_page = requests.get(f'https://markets.businessinsider.com{i[0]}', timeout=5).text
        company_page_soup = BeautifulSoup(html_text_page, "html.parser")

        price = company_page_soup.find('span', class_='price-section__current-value').text
        price = round(float(price.replace(",", "")) * one_dollar, 2)

        take_ticker = str(company_page_soup.title.text).split()[0].strip()
        pe_data_heap = company_page_soup.find_all('div', class_='snapshot__data-item')
        pe_data = None
        low_week = high_week = 0
        for elm in pe_data_heap:
            if 'P/E Ratio' in str(elm).strip():
                pe_data = str(elm.text).strip().split()[0]
                clean_pe_data = float(pe_data.replace(",", ''))
            if '52 Week Low' in str(elm).strip():
                low_week = str(elm.text).strip().split()[0]
                clean_low_week = low_week.replace(",", '')
            if '52 Week High' in str(elm).strip():
                high_week = str(elm.text).strip().split()[0]
                clean_high_week = high_week.replace(",", '')

        potential_profit = round((float(clean_high_week) - float(clean_low_week)) / float(clean_low_week) * 100, 2)
        new_company = Company(key, take_ticker, price, company_name_dict[key][1], clean_pe_data, potential_profit)
        company_list.append(new_company)
    return company_list


def find_dollar_price()->float:
    # get central bank valute data
    now = datetime.datetime.now()
    day = now.day
    year = now.year
    month = 0

    if now.month < 10:
        month = '0' + str(now.month)

    cb_url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"

    cb_data_text = requests.get(cb_url, timeout=5).text
    currencies_soup = BeautifulSoup(cb_data_text, "lxml")
    currencies = currencies_soup.find_all('valute')

    one_dollar_price = 0
    for elm in currencies:
        if elm.find('charcode').text == 'USD':
            one_dollar_price = elm.find('value').text
            one_dollar_price = float(one_dollar_price.replace(",", "."))

    return one_dollar_price


one_dollar = 0


if __name__ == "__main__":

    start_time = time.time()
    print(start_time)

    one_dollar = find_dollar_price()

    url = 'https://markets.businessinsider.com/index/components/s&p_500'

    company_list = list()

    html_text = requests.get(url, timeout=5).text
    title_page_content = BeautifulSoup(html_text, "html.parser")

    # get page numbers
    num_of_pages = title_page_content.select(".finando_paging a")

    page_num_list = list()
    for elm in num_of_pages:
        page_num = BeautifulSoup(str(elm), 'html.parser').a.text
        if str(page_num).isdigit():
            page_num_list.append(int(page_num))

    with Pool(48) as p:
        company_list.append(p.map(walk_on_the_page, range(min(page_num_list), max(page_num_list))))

    company_list = [elm for subarray in company_list for elm in subarray]
    company_list = [elm for subarray in company_list for elm in subarray]

    company_list.sort(key=operator.attrgetter('price'))
    top_price_list = company_list[len(company_list) - 10:]
    top_price_list.reverse()

    with open('price.json', 'w') as outfile:
        print("Top price")
        counter = 0
        for i in top_price_list:
            print(counter, i)
            counter += 1
            json.dump(i.toJSON(), outfile)

    company_list.sort(key=operator.attrgetter('pe_ratio'))
    top_pe_list = company_list[:10]
    with open('top_pe_ratio.json', 'w') as outfile:
        print("Top pe")
        counter = 0
        for i in top_pe_list:
            print(counter, i)
            counter += 1
            json.dump(i.toJSON(), outfile)

    company_list.sort(key=operator.attrgetter('one_year_gain'))
    top_one_year_profit_list = company_list[len(company_list) - 10:]
    top_one_year_profit_list.reverse()
    with open('top_one_year_gain.json', 'w') as outfile:
        print("Top one year gain")
        counter = 0
        for i in top_one_year_profit_list:
            print(counter, i)
            counter += 1
            json.dump(i.toJSON(), outfile)

    company_list.sort(key=operator.attrgetter('potential_52_week_profit'))
    top_one_year_profit_list = company_list[len(company_list) - 10:]
    top_one_year_profit_list.reverse()
    with open('top_25_week_profit.json', 'w') as outfile:
        print("Top 52 week deal profit")
        counter = 0
        for i in top_one_year_profit_list:
            print(counter, i)
            counter += 1
            json.dump(i.toJSON(), outfile)

    result_time = time.time() - start_time

    print("Time of execution = ", result_time)
