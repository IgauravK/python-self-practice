import requests
import logging

from Pages.bookspage import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scrapping')

logger.info('Loading book list...')

page_content = requests.get('http://books.toscrape.com').content

page = BookPage(page_content)

'''for books in page.Books:
    print(books)'''

books = page.Books

for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page content.')
    page = BookPage(page_content)
    books.extend(page.Books)