from bs4 import BeautifulSoup
import requests

import datetime



now = datetime.datetime.now()
print("year", now.year)
print("month", now.month)
print("day", now.day)

cb_url= f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={now.day}/{now.month}/{now.year}"

cb_data_text = requests.get(cb_url, timeout=5).text
title_page_content = BeautifulSoup(cb_data_text, "html.parser")

print(title_page_content)

# * Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
# * Код компании (справа от названия компании на странице компании)
# * P/E компании (информация находится справа от графика на странице компании)
# * Годовой рост/падение компании в процентах (основная таблица)
# * Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)

url = 'https://markets.businessinsider.com/index/components/s&p_500'


class Company:

    name = str
    ticker = str
    price = float
    one_year_gain = str
    pe_ratio = float
    potential_52_week_profit = str

    def __init__(self, name, ticker, price, one_year_gain, pe_ratio, potential_52_week_profit):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.one_year_gain = one_year_gain
        self.pe_ratio = pe_ratio
        self.potential_52_week_profit = potential_52_week_profit

    def __repr__(self):
        return str(self.__dict__)


company_list = list()

html_text = requests.get(url, timeout=5).text
title_page_content = BeautifulSoup(html_text, "html.parser")


print("ДОСТАЕМ СТРАНИЦЫ")
num_of_pages = title_page_content.select(".finando_paging a")

page_num_list = list()
for elm in num_of_pages:
    page_num = BeautifulSoup(str(elm), 'html.parser').a.text
    if str(page_num).isdigit():
        page_num_list.append(int(page_num))

print(page_num_list)

for i in range(1, max(page_num_list)):
    print(f"page number {i}")
    company_name_dict = dict()
    html_text_page = requests.get(f'https://markets.businessinsider.com/index/components/s&p_500?p={i}', timeout=5).text

    content_from_page = BeautifulSoup(html_text_page, "html.parser")

    table_data = content_from_page.find('table', {'class': 'table table__layout--fixed'})

    print("Достаю ссылки на компании c именами")
    # year_profit = 0
    print("ИМЕНА С ГЛАВНОЙ СТРАНИЦЫ")
    for data in table_data.findAll('tr')[1:]:
        name = data.findAll('td')[0].text
        year_profit = data.findAll('td')[7].text.split()[1]
        link = data.find('td', class_='table__td table__td--big').a.get('href')
        company_name_dict[name.strip()] = [link.strip(), year_profit.strip()]
    print(company_name_dict)

    print("\nДОСТАЮ ДАННЫЕ С СТРАНИЦЫ САМОЙ КОМПАНИИ")
    for key in company_name_dict:

        i = company_name_dict[key]
        html_text_page = requests.get(f'https://markets.businessinsider.com{i[0]}', timeout=5).text
        company_page_soup = BeautifulSoup(html_text_page, "html.parser")

        price = company_page_soup.find('span', class_='price-section__current-value').text
        take_ticker = str(company_page_soup.title.text).split()[0]
        pe_data_heap = company_page_soup.find_all('div', class_='snapshot__data-item')
        pe_data = low_week = high_week = 0
        for elm in pe_data_heap:
            if 'P/E Ratio' in str(elm).strip():
                pe_data = elm.text
            if '52 Week Low' in str(elm).strip():
                low_week = str(elm.text).strip().split()[0]
                clean_low_week = low_week.replace(",", '')
            if '52 Week High' in str(elm).strip():
                high_week = str(elm.text).strip().split()[0]
                clean_high_week = high_week.replace(",", '')

        potential_profit = round((float(clean_high_week) - float(clean_low_week))/float(clean_low_week)*100, 2)
        # company_name_dict[key].append(str(take_ticker).strip())
        # company_name_dict[key].append(str(pe_data).strip().split()[0])
        # company_name_dict[key].append(price)
        # company_name_dict[key].append(potential_profit)
        potential_52_week_profit = str(potential_profit) + '%'
        new_company = Company(key, str(take_ticker).strip(),  price, company_name_dict[key][1], str(pe_data).strip().split()[0], potential_52_week_profit)
        # print(company_name_dict)
        company_list.append(new_company)
    break

for i in company_list:
    print(i)
















