from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
        return 1 <= score <= 1000
    except Exception as e:
        return False
    finally:
        driver.quit()

def main_function():
    if tests():
        return 0
    else:
        return -1