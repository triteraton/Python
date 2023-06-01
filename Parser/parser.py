from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup

actors_names = []
actors_films = []
for i in range(2):
    actor_name = input("Enter the url code of actor {}: ".format(i+1))
    url = "https://www.imdb.com/name/{}/".format(actor_name)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.ok:
        response_content = response.content
        soup = BeautifulSoup(response_content, "html.parser")
        films_count = int(soup.body.find("div", {"class": "ipc-accordion sc-5cecff0c-0 WeRzr date-credits-accordion ipc-accordion--base ipc-accordion--dividers-none ipc-accordion--pageSection"}).find("li", {"class": "ipc-inline-list__item credits-total"}).text)
        actor_name = soup.body.find("h1", {"data-testid": "hero__pageTitle"}).text
        actors_names.append(actor_name)
        
        if films_count > 15: 
            driver = webdriver.Edge()
            driver.get(url)
            #page_height = driver.execute_script("return document.body.scrollHeight")
            if soup.body.find("ul", {"class": "ipc-inline-list ipc-inline-list--show-dividers sc-afe43def-4 kdXikI baseAlt"}).text.find("Actor") != -1:
                button = driver.find_element(By.XPATH, value='//button[@data-testid="nm-flmg-paginated-all-actor"]')
                driver.execute_script("arguments[0].click();", button)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.invisibility_of_element_located((By.XPATH, '//button[@data-testid="nm-flmg-paginated-all-actor"]')))
            else:
                button = driver.find_element(By.XPATH, value='//button[@data-testid="nm-flmg-paginated-all-actress"]')
                driver.execute_script("arguments[0].click();", button)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.invisibility_of_element_located((By.XPATH, '//button[@data-testid="nm-flmg-paginated-all-actress"]')))
            #wait.until(lambda driver: driver.execute_script("return document.body.scrollHeight") > page_height)
            new_response_content = driver.page_source
            driver.quit()
            soup = BeautifulSoup(new_response_content, "html.parser")
        div = soup.body.find("div", {"class": "ipc-accordion sc-5cecff0c-0 WeRzr date-credits-accordion ipc-accordion--base ipc-accordion--dividers-none ipc-accordion--pageSection"})
        all_a = div.find_all("a")
        films_list = []
        for a in all_a:
            if a.text:
                films_list.append(a.text)
        actors_films.append(films_list)
    else:
        print("Failed to get response from the site") 

common_films = []
common_films = list(set(actors_films[0]).intersection(set(actors_films[1])))

print("Films of actor {}:\n".format(actors_names[0]), ", ".join(actors_films[0]))
print("Films of actor {}:\n".format(actors_names[1]), ", ".join(actors_films[1]))
print("Common films of two actors:",  ", ".join(common_films))