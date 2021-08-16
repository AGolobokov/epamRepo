from bs4 import BeautifulSoup
import requests
import datetime
import operator
import json
import time
import asyncio

start_time = time.time()

# get central bank valute data
now = datetime.datetime.now()
day = now.day
year = now.year
month = 0

if now.month < 10:
    month = '0'+str(now.month)

cb_url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}"

cb_data_text = requests.get(cb_url, timeout=10).text
currencies_soup = BeautifulSoup(cb_data_text, "lxml")
currencies = currencies_soup.find_all('valute')

one_dollar_price = 0
for elm in currencies:
    if elm.find('charcode').text == 'USD':
        one_dollar_price = elm.find('value').text
        one_dollar_price = float(one_dollar_price.replace(",", "."))


url = 'https://markets.businessinsider.com/index/components/s&p_500'


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
        self.price = round(one_dollar_price * float(price), 2)
        self.one_year_gain = one_year_gain
        self.pe_ratio = pe_ratio
        self.potential_52_week_profit = potential_52_week_profit

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


company_list = list()

html_text = requests.get(url, timeout=10).text
title_page_content = BeautifulSoup(html_text, "html.parser")


# get page numbers
num_of_pages = title_page_content.select(".finando_paging a")

page_num_list = list()
for elm in num_of_pages:
    page_num = BeautifulSoup(str(elm), 'html.parser').a.text
    if str(page_num).isdigit():
        page_num_list.append(int(page_num))



async def get(url):
    html_text_page = requests.get(url, timeout=5).text
    company_page_soup = BeautifulSoup(html_text_page, "html.parser")
    return company_page_soup

# get data of company
for i in range(min(page_num_list), max(page_num_list) + 1):
    # get data from main page
    print(f"page number {i}")
    company_name_dict = dict()
    html_text_page = requests.get(f'https://markets.businessinsider.com/index/components/s&p_500?p={i}', timeout=5).text

    content_from_page = BeautifulSoup(html_text_page, "html.parser")
    table_data = content_from_page.find('table', {'class': 'table table__layout--fixed'})

    # get link, year profit and name
    for data in table_data.findAll('tr')[1:]:
        name = data.findAll('td')[0].text
        year_profit = data.findAll('td')[7].text.split()[1].strip()
        clean_year_profit = float(year_profit.replace("%", ""))
        link = data.find('td', class_='table__td table__td--big').a.get('href')
        company_name_dict[name.strip()] = [link.strip(), clean_year_profit]

    loop = asyncio.get_event_loop()

    coroutines = [get(f'https://markets.businessinsider.com{company_name_dict[key][0]}') for key in company_name_dict]

    results = loop.run_until_complete(asyncio.gather(*coroutines))

    for elm in results:

        price = elm.find('span', class_='price-section__current-value').text
        price = float(price.replace(",", ""))
        take_ticker = str(elm.title.text).split()[0].strip()
        pe_data_heap = elm.find_all('div', class_='snapshot__data-item')
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

        potential_profit = round((float(clean_high_week) - float(clean_low_week))/float(clean_low_week)*100, 2)
        new_company = Company("Name", take_ticker,  price, 0.0, clean_pe_data, potential_profit)
        company_list.append(new_company)


company_list.sort(key=operator.attrgetter('price'))
top_price_list = company_list[len(company_list)-10:]
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
top_one_year_profit_list = company_list[len(company_list)-10:]
top_one_year_profit_list.reverse()
with open('top_one_year_gain.json', 'w') as outfile:
    print("Top one year gain")
    counter = 0
    for i in top_one_year_profit_list:
        print(counter, i)
        counter += 1
        json.dump(i.toJSON(), outfile)


company_list.sort(key=operator.attrgetter('potential_52_week_profit'))
top_one_year_profit_list = company_list[len(company_list)-10:]
top_one_year_profit_list.reverse()
with open('top_25_week_profit.json', 'w') as outfile:
    print("Top 52 week deal profit")
    counter = 0
    for i in top_one_year_profit_list:
        print(counter, i)
        counter += 1
        json.dump(i.toJSON(), outfile)

result_time = time.time() - start_time
print("Time of execution: ", result_time)