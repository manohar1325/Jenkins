import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://in.bookmyshow.com/explore/movies-nellore")

movie_names = driver.find_elements(By.XPATH, "//div[@class = 'style__StyledText-sc-7o7nez-0 dxpBCo']")

for index, movie in enumerate(movie_names):
    print(f"{index + 1}.{movie.text}")


