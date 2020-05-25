from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.quotes_pageB import QuotesPage, InvalidTagForAuthorError
try:
    author = input('Enter the author: ')
    tag = input("Enter tag: ")
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)
    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("Unknown Error")




'''#chrome = webdriver.Chrome(executable_path="/Users/Baba/chromedriver")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = input('Enter the author: ')
page.select_author(author)

tags = page.get_available_tag()
print("Select one: [{}]".format(' | '.join(tags)))
selected_tag = input("Enter tag: ")

page.select_tag(selected_tag)

page.search_button.click()
print(page.quotes)'''


