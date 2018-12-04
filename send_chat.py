import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    options = Options()
    #options.add_argument('-headless')
    driver = Firefox(executable_path='C:\\Program Files (x86)\\geckodriver.exe', firefox_options=options)
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://www.chatwork.com/')
    wait.until(expected.visibility_of_element_located((By.NAME, 'email'))).send_keys('user_name')
    wait.until(expected.visibility_of_element_located((By.NAME, 'password'))).send_keys('user_password')
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, 'input.new-theme_button'))).click()
    time.sleep(3)
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-rid="56566778"]'))).click()
    time.sleep(3)
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[id="_chatText"]'))).send_keys('Testtttt!')
    wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, 'div[id="_sendButton"]'))).click()
    #print(driver.page_source)
    #driver.quit()
