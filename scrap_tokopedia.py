from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

if __name__ == "__main__":
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='C:\\Program Files (x86)\\geckodriver.exe', firefox_options=options)
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://github.com/TheDancerCodes')
    # wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('nokia' + Keys.ENTER)
    # result = driver.find_elements_by_xpath("//div[@class='_1lUX-bZg']")
    # print(result)

    # Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = driver.find_elements_by_xpath("//a[@class='text-bold']")

# List Comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

# print response in terminal
print('TITLES:')
print(titles, '\n')


# Get all of the pinned repo languages
language_element = driver.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("LANGUAGES:")
print(languages, '\n')

# Pair each title with its corresponding language using zip function and print each pair
for title, language in zip(titles, languages):
	print("RepoName : Language")
	print(title + ": " + language, '\n')
