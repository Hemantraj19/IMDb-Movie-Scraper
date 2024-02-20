from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    options=chrome_options,
)
driver.get("https://www.imdb.com/")


menu = driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]')
menu.click()


movie_by_genre = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[4]/span',
        )
    )
)

movie_by_genre.click()

generes_div = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="__next"]/main/div/section/div/section/div/div[1]/section[1]/div[2]/div[2]',
        )
    )
)

generes_a = generes_div.find_elements(By.CSS_SELECTOR, "a")

genres = []
for genre in generes_a:
    span_element = genre.find_element(By.CSS_SELECTOR, "span")
    genres.append(span_element.text)

print("Which genre do you want to watch: ")
for i in range(len(genres)):
    print(f"{i}. for {genres[i]}")

user_genre = int(input("Enter your choice: "))

generes_a[user_genre].click()

scroll_amount = 200  # Adjust this value according to your needs
driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
time.sleep(2)

sort_by = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[1]/div[1]/span/span',
        )
    )
)

sort_by.click()

print("\nSort By: ")

sort_by_select = driver.find_element(By.CSS_SELECTOR, "select#adv-srch-sort-by")

options = sort_by_select.find_elements(By.CSS_SELECTOR, "option")

for i in range(1, len(options)):
    print(f"{i}. for {options[i].text}")

choice = int(input("Enter your choice: "))

options[choice].click()

movies = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul',
        )
    )
)

movie_list = movies.find_elements(By.CSS_SELECTOR, "li")

movies_title = []
movies_release_year = []
movies_description = []

for movie in movie_list:
    movie_title = movie.find_element(By.CSS_SELECTOR, "div div a h3").text
    release_year = movie.find_element(By.CSS_SELECTOR, "span.sc-be6f1408-8").text
    description_element = movie.find_elements(
        By.CSS_SELECTOR, "div div div.ipc-html-content-inner-div"
    )
    if description_element:
        description = description_element[0].text
    else:
        description = "No description"
    movies_title.append(movie_title)
    movies_release_year.append(release_year)
    movies_description.append(description)

driver.quit()


sheety_endpoint = "your sheety endpoint"

for title, year, desc in zip(movies_title, movies_release_year, movies_description):
    sheety_data = {
        "movie": {
            "Movie Name": title,
            "Release Year": year,
            "Description": desc,
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheety_data)
    print(response.text)
