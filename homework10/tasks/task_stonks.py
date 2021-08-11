from bs4 import BeautifulSoup
import requests

# * Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
# * Код компании (справа от названия компании на странице компании)
# * P/E компании (информация находится справа от графика на странице компании)
# * Годовой рост/падение компании в процентах (основная таблица)
# * Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)

url = 'https://markets.businessinsider.com/index/components/s&p_500'

html_text = requests.get(url, timeout=5).text

title_page_content = BeautifulSoup(html_text, "html.parser")


company_name_dict = dict()
first_page_company_name_link = list()


new_soup = 0

name_of_company = title_page_content.find_all('td', class_='table__td table__td--big')

for link in name_of_company:
    for elm in link.find_all('a'):
        first_page_company_name_link.append(elm.get('href'))
print(first_page_company_name_link)

company_page_data = dict()
for i in first_page_company_name_link:
    html_text_page = requests.get(f'https://markets.businessinsider.com{i}', timeout=5).text
    # company_page_data[i] = html_text_page
    company_page_soup = BeautifulSoup(html_text_page, "html.parser")
    take_ticker = company_page_soup.find('span', class_='price-section__category').text
    pe_data = company_page_soup.find_all('div', class_='snapshot__data-item')
    print(take_ticker, pe_data)
    break
print(company_page_data)

for elm in name_of_company:
    neme_soup = BeautifulSoup(str(elm), "html.parser")
    company_name_dict[neme_soup.a.text] = list()
print(company_name_dict)


num_of_pages = title_page_content.select(".finando_paging a")
count_pages = title_page_content.find('div', class_='finando_paging margin-top--small')


page_num_list = list()
for elm in num_of_pages:
    page_num_list.append(BeautifulSoup(str(elm), 'html.parser').a.text)

print(page_num_list)



# my_dict = dict()
# for i in page_num:
#     html_text_page = requests.get(f'https://markets.businessinsider.com/index/components/s&p_500?p={i}', timeout=5).text
#     my_dict[i] = html_text_page
#
# print(my_dict)
# for key in my_dict:
#     print("key_page =", key)
#     print("value_page = ", my_dict[key])


