import re
import logging
from Locators.booklocator import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from html')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name} {self.price}, ({self.rating} stars)>'

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        return self.parent.select_one(locator).attrs['title']
        logger.info('Found book name.')

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        logger.debug(f'Item price element found, `{item_price}`')
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        logger.info('Found book price.')
        return float(matcher.group(1))


    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        logger.debug(f'Found rating class, `{rating_classes}`.')
        logger.debug('Converting to integer for sorting.')
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.info(f'Found book rating, `{rating_number}`.')
        return rating_number

