import requests
from bs4 import BeautifulSoup
import logging

# Настройка логирования
logging.basicConfig(filename='google_dork_search.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')

# Функция для выполнения поиска с использованием Google Dork
def google_dork_search(query):
    
    url = f'https://www.google.com/search?q=filetype:pdf+{query}&num=50'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Обработка результатов
        search_results = soup.find_all('div', class_='tF2Cxc')
        if not search_results:
            logging.info("Нет результатов по запросу.")
            return

        for result in search_results:
            title = result.h3.text
            link = result.a['href']
            print(f'Title: {title}')
            logging.info(f'Title: {title}')
            print(f'Link: {link}')
            logging.info(f'Link: {link}')
            print('----------------------------------------------------------------------------------------')
            logging.info('----------------------------------------------------------------------------------------')

    except requests.exceptions.RequestException as e:
        logging.error(f'Произошла ошибка при выполнении запроса: {e}')

    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')

if __name__ == "__main__":
    user_query = input("Введите ключевое слово для поиска: ")
    google_dork_search(user_query)
