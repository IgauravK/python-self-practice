#from bs4 import BeautifulSoup

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self, browser):
        self.browser = browser
        #self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocators.QUOTE
            )
        ]

    '''@property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]'''