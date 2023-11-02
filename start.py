import requests
from bs4 import BeautifulSoup

# Функция для выполнения поиска с использованием Google Dork
def google_dork_search(query):
    # Замените `ваш_ключ_API` на ваш ключ API, если используете его
    #url = f'https://www.googleapis.com/customsearch/v1?key=ваш_ключ_API&cx=ваш_пользовательский_идентификатор_cx&q={query}'

    # Если вы не используете ключ API, вы можете отправить запрос напрямую
    url = f'https://www.google.com/search?q={query}'
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
            print('---')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    user_query = input("Введите запрос для поиска: ")
    google_dork_search(user_query)