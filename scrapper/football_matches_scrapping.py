from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#scraping data from tipsport.cz
def scrape_data(driver):
    matches_played = [match.text for match in driver.find_elements(By.CSS_SELECTOR, "span.o-matchRow__matchName") if match.text != "1.anglická f.l. 2023/2024 - celkově"]
    odds = [float(odd.text) if odd.text != "" else 0 for odd in driver.find_elements(By.CSS_SELECTOR, "div.btnRate")]
    individ_odds = [odds[i:i+5] for i in range(0, len(odds), 5)]

    driver.quit()

    data = dict(zip(matches_played, individ_odds))
    return data


def english_premier_league():
    #webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-anglicka-liga-118")

    driver.implicitly_wait(10) #waiting for the page to load
    return scrape_data(driver)

def german_bundesliga():
    #webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-nemecka-liga-130")
    
    driver.implicitly_wait(10) #waiting for the page to load
    return scrape_data(driver)

def spanish_la_liga():
    #webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-spanelska-liga-140")
    
    driver.implicitly_wait(10) #waiting for the page to load
    return scrape_data(driver)

def italian_serie_a():
    #webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-italska-liga-127")
    
    driver.implicitly_wait(10) #waiting for the page to load
    return scrape_data(driver)

def french_ligue_1():
    #webdriver setup
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-francouzska-liga-124")
    
    driver.implicitly_wait(10) #waiting for the page to load
    return scrape_data(driver)