from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.quotes_pageB import QuotesPage


chrome = webdriver.Chrome(ChromeDriverManager().install())
print (chrome)

#chrome = webdriver.Chrome(executable_path="/Users/Baba/chromedriver")
chrome.get("https://hotels.cloudbeds.com/auth/login")


