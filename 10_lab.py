from requests import get
from requests.exceptions import HTTPError,ConnectionError,Timeout,RequestException
from pprint import pprint

API_KEY = 'dc6db38643774115914dbff1038cfb56'

try:
    end_point= 'https://newsapi.org/v2/everything?q=tesla&from=2026-01-16&sortBy=publishedAt&apiKey=dc6db38643774115914dbff1038cfb56'
    response= get(end_point,timeout=6000)
    data = response.json()
    pprint(data)
    print(
        f'Author: {data["articles"][0]["author"]}\n'
        f'Title: {data["articles"][0]["title"]}\n'
    )


except HTTPError as err:
    print(f'HTTPError {err}')
except ConnectionError as err:
    print(f'ConnectionError {err}')
except Timeout as err:
    print(f'TimeoutError {err}')
except RequestException as err:
    print(f'General Error {err}')

# author_name = input("Enter Author Name: ")
# for article in data.get["articles"]:
#         if article.get["author"] == author_name:
#             pprint(article)

results = [article for article in data.get("articles") if article.get["author"] == author_name]

for result in results:
    pprint(result)
