import requests
from bs4 import BeautifulSoup

# Функция для выполнения поиска с использованием Google Dork
def google_dork_search(query):

    url = f'https://www.google.com/search?q=filetype:pdf+{query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Обработка результатов
        search_results = soup.find_all('div', class_='tF2Cxc')
        for result in search_results:
            title = result.h3.text
            link = result.a['href']
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('----------------------------------------------------------------------------------------')

    except requests.exceptions.RequestException as e:
        print(f'Произошла ошибка при выполнении запроса: {e}')

    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == "__main__":
    user_query = input("Введите ключ-слово для поиска: ")
    google_dork_search(user_query)