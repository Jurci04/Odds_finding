from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

## @brief scraping data from tipsport.cz
#  @param driver webdriver set up in the function scrape_league
#  @return dictionary with matches as keys and odds as values
def scrape_data(driver):
    matches_played = [match.text for match in driver.find_elements(By.CSS_SELECTOR, "span.o-matchRow__matchName") if match.text != "1.anglická f.l. 2023/2024 - celkově"]
    odds = [float(odd.text) if odd.text != "" else 0 for odd in driver.find_elements(By.CSS_SELECTOR, "div.btnRate")]
    individ_odds = [odds[i:i+5] for i in range(0, len(odds), 5)]

    driver.quit()

    data = dict(zip(matches_played, individ_odds))
    return data

## @brief scraping data from from the given url
#  @param url url of the league
#  @return the function scrape_data 
def scrape_league(url):
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    
    driver.implicitly_wait(10)
    return scrape_data(driver)

#All the leagues so far:
    
def english_premier_league():
    EPL_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-anglicka-liga-118")
    return EPL_data

def german_bundesliga():
    ger_bundesliga_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-nemecka-liga-130")
    return ger_bundesliga_data

def spanish_la_liga():
    spanish_la_liga_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-spanelska-liga-140")
    return spanish_la_liga_data

def italian_serie_a():
    italian_serie_a_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-italska-liga-127")
    return italian_serie_a_data

def french_ligue_1():
    french_ligue_1_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-francouzska-liga-124")
    return french_ligue_1_data

def slovak_nike_liga():
    slovak_nike_liga_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-slovenska-liga-138")
    return slovak_nike_liga_data

def czech_1st_league():
    czech_1st_league_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-ceska-liga-120")
    return czech_1st_league_data

def dutch_eridivisie():
    dutch_eridivisie_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-nizozemska-liga-125")
    return dutch_eridivisie_data

def turkish_super_lig():
    turkish_super_lig_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-turecka-liga-142")
    return turkish_super_lig_data

def portugal_liga_nos():
    portugal_liga_nos_data = scrape_league("https://www.tipsport.cz/kurzy/fotbal/fotbal-muzi/1-portugalska-liga-133")
    return portugal_liga_nos_data