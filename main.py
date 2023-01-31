import getpass
from re import error

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")

loginElm = driver.find_element(
    by=By.ID,
    value="session_key"
)
passElm = driver.find_element(
    by=By.ID,
    value="session_password"
)
loginBtn = driver.find_element(
    By.CLASS_NAME,
    value="sign-in-form__submit-button",
)

# login = input("Insert the login: ")
pw = getpass.getpass("Insert the password: ", )

loginElm.send_keys("andrierlisondeveloper@gmail.com")
passElm.send_keys(pw)

driver.fullscreen_window()

loginBtn = driver.find_element(
    By.CLASS_NAME, value="sign-in-form__submit-button"
)

loginBtn.click()

searchField: WebElement = WebDriverWait(driver, timeout=3).until(
    lambda d: d.find_element(
        By.CLASS_NAME, "search-global-typeahead__input")
)

searchField.send_keys("Tech recruiter")

# Press enter
searchField.send_keys("\ue007")

connectBtns = driver.find_elements(By.CLASS_NAME, value="artdeco-button")

index = 1

for connectBtn in connectBtns:
    WebDriverWait(driver, 2)
    connectBtn.click()

driver.quit()
